"""
ITC project #1: smart-phone scraper.
This is a Data-Mining project.
We scrape "GSMarena" website for smartphone data, of two companies: Samsung and Apple.
handle robots:
https://docs.python.org/3/library/urllib.robotparser.html
"""

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import json
from gsmarena_conf import *
from time import sleep
from random import random

JSON_INDENT = 4
GSMARENA_ADAPTER = HTTPAdapter(max_retries=GSMARENA_MAX_RETRIES)
GSMARENA_ADAPTER.max_retries.respect_retry_after_header = False  # abort site retry command


def save_data(filename, data):
    """
    save output data into json file format
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=JSON_INDENT)


def get_pages(urls: list[str], batch_size=BATCH_SIZE,
              timeout_batch=REQUEST_BATCH_DELAY, timeout_single=REQUEST_SINGLE_DELAY) -> list[requests.models.Response]:
    """
    :inputs: list of url addresses, number of threads
    :return: list of responses
    """
    # send request header to fool not detectors
    # https://stackoverflow.com/questions/47956527/how-do-websites-detect-bots
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox
    # https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python
    # https://hacks.mozilla.org/2013/09/user-agent-detection-history-and-checklist/
    tmp_session = requests.Session()
    tmp_session.mount(prefix=MAIN_SITE, adapter=GSMARENA_ADAPTER)
    responses = []
    # sleep_flag = 0
    for idx, url in enumerate(urls):
        # print(url)
        # exit()
        # sleep_flag += 1
        # if batch_size < sleep_flag:
        #     print(f"batch sleep: {timeout_batch} sec.")
        #     # sleep(timeout_batch)
        #     sleep_flag = 0
        try:
            tmp_response = tmp_session.get(url, timeout=GSMARENA_TIMEOUT, headers=REQUEST_HEADER)
            # tmp_response = requests.get(url, headers=REQUEST_HEADER)
        except ConnectionError as e:
            print(e)
            print(f'ConnectionError: skip {url}')
        else:
            if not tmp_response.ok:
                print(f'ResponseError: skip {url}')
                continue
            responses.append(tmp_response)
        sleep_time = timeout_single  # + random() * timeout_single
        print(f"num_reqs: {idx + 1}/{len(urls)}, "
              f"status: {responses[-1].ok}, "
              f"sleep: {sleep_time} sec.")
        # sleep between requests
        sleep(sleep_time)
    # if sleep_flag > 0:
    #     print(f"batch sleep: {timeout_batch} sec.")
        # sleep(timeout_batch)
        # sleep_flag = 0

    return responses


def get_phone_list(pages: list[requests.models.Response]) -> list[str]:
    """
    return list of url addresses for each phone in search result.
    """
    soups = [BeautifulSoup(page.content, features="html.parser") for page in pages]
    return [MAIN_SITE + '/' + ele.a.get('href') for soup in soups
            for ele in soup.find('div', class_="makers").find_all('li')]


def get_phone_data(page: requests.models.Response) -> dict:
    """
    return all phone properties from website as a dict.
    """
    phone_data = dict()
    soup = BeautifulSoup(page.content, features='html.parser')
    phone_name = soup.find('h1', class_="specs-phone-name-title").text
    phone_data[phone_name] = dict()
    for table in soup.find('div', id='specs-list').find_all('table'):
        title = table.find('th').text
        phone_data[phone_name][title] = dict()
        for sub_table in table.find_all('tr'):
            if sub_table:
                key = sub_table.find('td', class_='ttl')
                val = sub_table.find('td', class_='nfo')
                if key and key.text != NON_BREAK_SPACE:
                    phone_data[phone_name][title][key.text.replace(NON_BREAK_SPACE, ' ')] = \
                        val.text.replace(NON_BREAK_SPACE, ' ')
                else:
                    if val:
                        try:
                            phone_data[phone_name][title]['other'].append(val.text.replace(NON_BREAK_SPACE, ' '))
                        except KeyError:
                            phone_data[phone_name][title]['other'] = []
                            phone_data[phone_name][title]['other'].append(val.text.replace(NON_BREAK_SPACE, ' '))

    return phone_data


def smartphones_scraper(brand: str) -> list[dict]:
    """
    scrape all iphone smartphone data from GSMarena and save data as json.
    """
    website_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, BRANDS['Samsung'], AVAILABLE, FORM_FACTOR)
                      for year in YEAR_RANGE]
    smartphones_search_pages = get_pages(website_search)
    smartphones_links = get_phone_list(smartphones_search_pages)

    # get smartphones data
    smartphones_pages = get_pages(smartphones_links[:100])
    smartphones_data = [get_phone_data(page) for page in smartphones_pages if page.ok]

    print(f"got all {brand} smartphones data")
    return smartphones_data


def main():
    # phones_data = smartphones_scraper(brand=APPLE)
    # save_data('apple_smartphones_data.json', phones_data)
    phones_data = smartphones_scraper(brand='Samsung')
    save_data('samsung_smartphones_data.json', phones_data)


if __name__ == "__main__":
    main()

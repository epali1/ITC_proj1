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

JSON_INDENT = 4
GSMARENA_ADAPTER = HTTPAdapter(max_retries=GSMARENA_MAX_RETRIES)
GSMARENA_ADAPTER.max_retries.respect_retry_after_header = False  # abort site retry command


def save_data(filename, data):
    """
    save output data into json file format
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=JSON_INDENT)


def get_pages(urls: list[str], timeout=REQUEST_DELAY) -> list[requests.models.Response]:
    """
    :inputs: list of url addresses, number of threads
    :return: list of responses
    """
    tmp_session = requests.Session()
    tmp_session.mount(prefix=MAIN_SITE, adapter=GSMARENA_ADAPTER)
    responses = []
    for idx, url in enumerate(urls):
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
        print(f"num_reqs: {idx + 1}/{len(urls)}, "
              f"status: {responses[-1].ok}, "
              f"sleep: {timeout} sec.")
        # sleep between requests
        sleep(timeout)

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
    smartphones_pages = get_pages(smartphones_links)
    smartphones_data = [get_phone_data(page) for page in smartphones_pages if page.ok]

    print(f"got all {brand} smartphones data")
    return smartphones_data


def main():
    # phones_data = smartphones_scraper(brand='Apple')
    # save_data('apple_smartphones_data.json', phones_data)
    phones_data = smartphones_scraper(brand='Samsung')
    save_data('samsung_smartphones_data.json', phones_data)


if __name__ == "__main__":
    main()

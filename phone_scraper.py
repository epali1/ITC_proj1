"""
ITC project #1: smart-phone scraper.
This is a Data-Mining project.
We scrape "GSMarena" website for smartphone data, of two companies: Samsung and Apple.

handle robots:
https://docs.python.org/3/library/urllib.robotparser.html
"""

import requests
from bs4 import BeautifulSoup
import json
from gsmarena_conf import *
from time import sleep

JSON_INDENT = 4


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
    how to handles connection errors. source:
    https://realpython.com/python-requests/#other-http-methods
    more issues:
    https://stackoverflow.com/questions/47397919/python-requests-with-httpadapter-is-halting-for-hours
    """
    responses = []
    for idx, url in enumerate(urls):
        try:
            responses.append(requests.get(url))
        except requests.exceptions.ConnectionError as e:
            print(e, f"\n sleep for {timeout} seconds and try again")
            sleep(timeout)
            responses.append(requests.get(url))

        sleep(timeout)
        print(f"num_reqs: {idx}/{len(urls)}, "
              f"status: {responses[-1].ok}, "
              f"sleep: {timeout} sec.")
        if not responses[-1].ok:
            exit(1)

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
    samsung_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, brand, AVAILABLE, FORM_FACTOR)
                      for year in YEAR_RANGE]
    samsung_search_pages = get_pages(samsung_search)
    samsung_links = get_phone_list(samsung_search_pages)

    # get smartphones data
    samsung_pages = get_pages(samsung_links)
    smartphones_data = [get_phone_data(page) for page in samsung_pages if page.ok]

    print(f"got all {brand} smartphones data")
    return smartphones_data


def main():
    # phones_data = smartphones_scraper(brand=APPLE)
    # save_data('apple_smartphones_data.json', phones_data)
    phones_data = smartphones_scraper(brand=SAMSUNG)
    save_data('samsung_smartphones_data.json', phones_data)


if __name__ == "__main__":
    main()

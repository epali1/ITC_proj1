"""
ITC project #1: smart-phone scraper.
This is a Data-Mining project.
We scrape "GSMarena" website for smartphone data, of two companies: Samsung and Apple.
"""

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import json
from gsmarena_conf import *

JSON_INDENT = 4


def save_data(filename, data):
    """
    save output data into json file format
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=JSON_INDENT)


def get_pages(urls: list[str]) -> list[requests.models.Response]:
    """
    :inputs: list of url addresses
    :return: list of responses
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        responses = executor.map(requests.get, urls)

    return list(responses)


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


def iphone_scraper() -> list[dict]:
    """
    scrape all iphone smartphone data from GSMarena and save data as json.
    """
    iphone_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, APPLE, AVAILABLE, FORM_FACTOR)
                     for year in YEAR_RANGE]
    iphone_search_pages = get_pages(iphone_search)
    print(iphone_search_pages)
    exit(0)
    iphone_links = get_phone_list(iphone_search_pages)

    # get phone data
    iphone_pages = get_pages(iphone_links)
    phone_data = [get_phone_data(page) for page in iphone_pages if page.ok]

    # all(map(lambda x: x.ok, iphone_pages))
    return phone_data


def main():
    phone_data = iphone_scraper()
    save_data('iphone_data.json', phone_data)


if __name__ == "__main__":
    main()

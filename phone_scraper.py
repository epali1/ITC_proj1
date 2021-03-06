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
import logging

GSMARENA_ADAPTER = HTTPAdapter(max_retries=GSMARENA_MAX_RETRIES)
GSMARENA_ADAPTER.max_retries.respect_retry_after_header = False  # abort site retry command

logger = logging.getLogger(LOG_NAME)


def activate_log(log_lvl='DEBUG', logfile=LOG_FILE, logoff=False):
    """
    control the logger properties.
    """
    logger.setLevel(LOG_LVL[log_lvl])

    if logfile:
        # Create handlers
        f_handler = logging.FileHandler(logfile, 'w')
        f_handler.setLevel(LOG_LVL['DEBUG'])
        # Create formatters and add it to handlers
        f_format = logging.Formatter(LOG_FILE_FORMAT)
        f_handler.setFormatter(f_format)
        # Add handlers to the logger
        logger.addHandler(f_handler)

    if not logoff:
        # Create handlers
        c_handler = logging.StreamHandler()
        c_handler.setLevel(LOG_LVL['INFO'])
        # Create formatters and add it to handlers
        c_format = logging.Formatter(LOG_CONSOLE_FORMAT)
        c_handler.setFormatter(c_format)
        # Add handlers to the logger
        logger.addHandler(c_handler)


def save_data(filename, data):
    """
    save output data into json file format
    """
    logger.info('Writing data into file')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=JSON_INDENT)

    logger.info('Done writing data into file')


def get_pages(urls, delay=REQUEST_DELAY):
    """
    return a list of responses from urls addresses
    """
    tmp_session = requests.Session()
    tmp_session.mount(prefix=MAIN_SITE, adapter=GSMARENA_ADAPTER)
    responses = []
    for idx, url in enumerate(urls):
        logger.info(f'Start url request {idx + 1} / {len(urls)}: {url}')
        try:
            tmp_response = tmp_session.get(url, timeout=GSMARENA_TIMEOUT, headers=REQUEST_HEADER)
        except ConnectionError as e:
            logger.warning(e)
            logger.warning(f'Url request failed (ConnectionError) skip')
        else:
            if not tmp_response.ok:
                logger.warning(f'Url request failed (ResponseError) skip')
                continue
            responses.append(tmp_response)

            logger.debug(f'Url request succeeded.')

        logger.debug(f'Site request delay: {delay}')
        sleep(delay)

    return responses


def get_phone_list(pages):
    """
    return list of url addresses for each phone in search result.
    """
    logger.info('Start getting all smartphone links from the search pages.')
    soups = [BeautifulSoup(page.content, features="html.parser") for page in pages]
    return [MAIN_SITE + '/' + ele.a.get('href') for soup in soups
            for ele in soup.find('div', class_="makers").find_all('li')]


def _get_table_val(val):
    """
    a helper function that organized the table value.
    """
    text = val.text.strip()
    if val.br:
        val = ", ".join(text.split('\r\n'))
    elif val.sup:
        val = "".join(map(str, val.contents))
    elif NON_BREAK_SPACE in text:
        val = ", ".join(text.split(f' {NON_BREAK_SPACE} {NON_BREAK_SPACE} '))
    else:
        val = text

    return val


def get_phone_data(page):
    """
    return all phone properties from website as a dict.
    """
    phone_data = dict()
    soup = BeautifulSoup(page.content, features='html.parser')
    phone_name = soup.find('h1', class_="specs-phone-name-title").text
    logger.info(f'Extract {phone_name} data from {page.url}')
    phone_data[phone_name] = dict()
    for table in soup.find('div', id='specs-list').find_all('table'):
        title = table.find('th').text
        logger.debug(f'Extract {phone_name}: {title}')
        phone_data[phone_name][title] = dict()
        for sub_table in table.find_all('tr'):
            if sub_table:
                key = sub_table.find('td', class_='ttl')
                val = sub_table.find('td', class_='nfo')
                if key and key.text != NON_BREAK_SPACE:
                    val = _get_table_val(val)
                    phone_data[phone_name][title][key.text.replace(NON_BREAK_SPACE, ' ')] = val

                else:
                    if val:
                        val = _get_table_val(val)
                        try:
                            phone_data[phone_name][title]['other'].append(val)
                        except KeyError:
                            phone_data[phone_name][title]['other'] = []
                            phone_data[phone_name][title]['other'].append(val)

    return phone_data


def smartphones_scraper(brand, year_min=YEAR_MIN, year_max=YEAR_MAX):
    """
    scrape all iphone smartphone data from GSMarena and save data as json.
    """
    # Add one to include current year.
    year_range = range(year_min, year_max + 1)
    logger.info(f"Start scraping all {brand} smartphone data from www.gsmarena.com")
    website_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, BRANDS[brand], AVAILABLE, FORM_FACTOR)
                      for year in year_range]
    logger.info(f"Prepared {len(website_search)} search links")
    smartphones_search_pages = get_pages(website_search)
    logger.info(f"Got {len(website_search)} search pages")
    if len(smartphones_search_pages) == 0:
        logger.critical('Didn\'t get any data. Exit the program...')
        exit(1)
    elif len(smartphones_search_pages) < len(website_search):
        logger.warning(f'Not all search links were retrieved {len(smartphones_search_pages)}/{len(website_search)}')
    smartphones_links = get_phone_list(smartphones_search_pages)
    logger.info(f"Prepared {len(smartphones_links)} smartphone links")
    # get smartphones data
    smartphones_pages = get_pages(smartphones_links)
    logger.info(f"Got {len(smartphones_pages)} smartphone pages")
    if len(smartphones_pages) == 0:
        logger.critical('Didn\'t get any data. Exit the program...')
        exit(1)
    elif len(smartphones_pages) < len(smartphones_links):
        logger.warning(f'Not all smartphones links were retrieved {len(smartphones_pages)}/{len(smartphones_links)}')
    smartphones_data = [get_phone_data(page) for page in smartphones_pages]
    logger.info(f"Done extracting {brand} smartphone data.")

    return smartphones_data


def main():
    print("This program scrape http://www.gsmarena.com for smartphones properties")
    activate_log()
    answer = input("Please, choose the Brand:\n1.Apple\n2.Samsung\n3.Apple and Samsung\n>>> ")
    while not (answer.strip() in ['1', '2', '3']):
        answer = input("Please, choose the Brand:\n1.Apple\n2.Samsung\n3.Apple and Samsung\n>>> ")

    answer = int(answer.strip())
    if answer == 1:
        phones_data = smartphones_scraper(brand='Apple')
        save_data('apple_smartphones_data.json', phones_data)
    elif answer == 2:
        phones_data = smartphones_scraper(brand='Samsung')
        save_data('samsung_smartphones_data.json', phones_data)
    elif answer == 3:
        phones_data = smartphones_scraper(brand='Apple')
        save_data('apple_smartphones_data.json', phones_data)
        phones_data = smartphones_scraper(brand='Samsung')
        save_data('samsung_smartphones_data.json', phones_data)


if __name__ == "__main__":
    main()

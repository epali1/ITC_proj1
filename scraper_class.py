"""
This file is part of ITC project #1: smart-phone scraper.
The file contain class for GSMarena.com scraper
"""
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import json
from gsmarena_conf import *
from time import sleep

JSON_INDENT = 4
GSMARENA_ADAPTER =



class SmartPhoneScraper:
    """
    create an object for GSMarena.com Samsung\\Apple Smartphone scraper.
    """

    def __init__(self):

        # site parameters
        self.main_url = MAIN_SITE
        self.result_page = RESULTS_PAGE

        # site search parameters
        self.brand = BRANDS
        self.available = AVAILABLE
        self.form_factor = FORM_FACTOR
        self.year_range = YEAR_RANGE

        # site request parameters
        self.delay = REQUEST_DELAY
        self.max_retries = GSMARENA_MAX_RETRIES
        self.timeout = GSMARENA_TIMEOUT
        self.header = {'User-Agent': 'Mozilla/5.0'}

        # set initial request
        self.session = requests.Session()
        self.session.mount(prefix=MAIN_SITE, adapter=GSMARENA_ADAPTER)

    def _find_smartphone_urls(self):
        """
        scrape a list of smartphone urls using site search page.
        """
        self.search_urls = [self.main_url +
                               self.result_page.format(year, year, self.brand['Samsung'],
                                                       self.available, self.form_factor)
                               for year in self.year_range]

    def _set_session(self):
        """
        set class private session.
        """
        self.adapter = HTTPAdapter(max_retries=self.max_retries)
        self.adapter.max_retries.respect_retry_after_header = False  # abort site retry command
        self.session = requests.Session()
        self.session.mount(prefix=MAIN_SITE, adapter=GSMARENA_ADAPTER)

    def _find_smartphone_pages(self):
        """
        return list of url addresses for each phone in search result.
        """
        soups = [BeautifulSoup(page.content, features="html.parser") for page in self.search_pages]
        self.smartphone_urls = [MAIN_SITE + '/' + ele.a.get('href') for soup in soups
                for ele in soup.find('div', class_="makers").find_all('li')]

    def request_page(self, urls):
        """
         :inputs: list of url addresses, number of threads
         :return: list of responses
         """
        self._set_session()
        responses = []
        for idx, url in enumerate(urls):
            try:
                tmp_response = self.session.get(url, timeout=self.timeout, headers=self.header)
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
                  f"sleep: {self.timeout} sec.")
            # sleep between requests
            sleep(self.timeout)

        return responses

    def save_data_as_json(self, filename):
        """
        save output data into json file format
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.smartphone_data, f, ensure_ascii=False, indent=JSON_INDENT)


    def scrape_smartphone_data(self):
        pass


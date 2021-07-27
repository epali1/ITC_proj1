import os

import pytest
from test_data import *
import sys

sys.path.append('../')
from gsmarena_conf import *
import phone_scraper


@pytest.fixture()
def setup():
    method_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    print("Executing test with name:  ", method_name)


def test_search_urls(setup):
    website_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, BRANDS['Samsung'], AVAILABLE, FORM_FACTOR)
                      for year in YEAR_RANGE]
    assert len(website_search) != 0


def test_get_search_pages(setup):
    response = phone_scraper.get_pages(test_website_urls, timeout=REQUEST_DELAY)
    assert len(response) != 0
    res = []
    for i in range(0, len(response)):
        status = response[i].status_code
        res.append(status)

    for i in range(0, len(res)):
        assert res[i] is 200


def test_get_phones_list(setup):
    response = phone_scraper.get_pages(test_website_urls, timeout=REQUEST_DELAY)
    phones_list = phone_scraper.get_phone_list(response)
    assert len(phones_list) != 0


def test_get_smartphone_pages(setup):
    response = phone_scraper.get_pages(test_phones_links)
    assert len(response) != 0
    res = []
    for i in range(0, len(response)):
        status = response[i].status_code
        res.append(status)

    for i in range(0, len(res)):
        assert res[i] is 200


def test_get_smartphone_data(setup):
    smartphones_pages = phone_scraper.get_pages(test_phones_links)

    smartphones_data = [phone_scraper.get_phone_data(page) for page in smartphones_pages if page.ok]

    assert len(smartphones_data) != 0

    for i in range(0, len(smartphones_data)):
        assert len(smartphones_data[i]) != 0


def test_save_data(setup):
    phone_scraper.save_data('test_smartphone_data.json', test_phones_data)

    check_file = os.stat("test_smartphone_data.json").st_size
    assert check_file != 0


def test_smartphone_scraper(setup):
    phones_data = phone_scraper.smartphones_scraper(brand=brand_samsung)
    assert phones_data is not None

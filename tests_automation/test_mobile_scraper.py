import pytest
import os
from tests_automation.test_data import *
from phone_scraper import *
from random import choices


def get_req(url, delay=REQUEST_DELAY):
    """
    helper function to test site responses
    """
    response = requests.head(url, headers=REQUEST_HEADER)
    sleep(delay)
    return response


@pytest.fixture()
def setup():
    method_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    print("Executing test with name:  ", method_name)


def test_search_urls(setup):
    """
    check if generated links are accurate.
    """
    website_search = [MAIN_SITE + RESULTS_PAGE.format(year, year, BRANDS[brand_samsung], AVAILABLE, FORM_FACTOR)
                      for year in YEAR_RANGE]
    assert len(website_search) != 0


def test_get_search_pages(setup):
    """
    test three web_search random links
    """
    responses = get_pages(choices(test_website_urls, k=3), delay=REQUEST_DELAY)
    assert len(responses) != 0
    assert all([response.ok for response in responses])


def test_search_pages_responses(setup):
    """
    test the responses of all web_search links.
    """
    responses = [get_req(url, delay=REQUEST_DELAY) for url in test_website_urls]
    assert all([response.ok for response in responses])


def test_get_phones_list(setup):
    """
    test get_phones_list function on three random links
    """
    responses = get_pages(choices(test_website_urls, k=3), delay=REQUEST_DELAY)
    phones_list = get_phone_list(responses)
    assert len(phones_list) != 0


def test_get_phones_list_accuracy(setup):
    """
    test if number of the return number smartphone links is valid.
    """
    test_year = 2015
    url = MAIN_SITE + RESULTS_PAGE.format(test_year, test_year, BRANDS[brand_samsung], AVAILABLE, FORM_FACTOR)
    response = get_pages([url], delay=REQUEST_DELAY)
    phones_list = get_phone_list(response)
    assert len(phones_list) == number_of_apple_smartphones_2015_links


def test_get_smartphone_pages(setup):
    """
    test three smartphone random links
    """
    responses = get_pages(choices(test_phones_links, k=3))
    assert len(responses) != 0
    assert all([response.ok for response in responses])


def test_smartphone_pages_responses(setup):
    """
    test the responses of all smartphone links.
    """
    responses = [get_req(url, delay=REQUEST_DELAY) for url in test_phones_links]
    assert len(responses) != 0
    assert all([response.ok for response in responses])


def test_get_smartphone_data(setup):
    """
    check, for three random smartphone links, if some data retrieved.
    """
    smartphones_pages = get_pages(choices(test_phones_links, k=3))
    smartphones_data = [get_phone_data(page) for page in smartphones_pages]
    assert len(smartphones_data) != 0
    for i in range(0, len(smartphones_data)):
        assert len(smartphones_data[i]) != 0


def test_save_data(setup):
    """
    check if any data saved in the output file.
    """
    save_data('test_smartphone_data.json', test_phones_data)
    check_file = os.stat("test_smartphone_data.json").st_size
    assert check_file != 0


def test_smartphone_scraper(setup):
    """
    check if the main function "smartphones_scraper" return value
    """
    phones_data = smartphones_scraper(brand=brand_apple)
    assert phones_data is not None

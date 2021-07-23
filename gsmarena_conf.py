"""
This is config file for "GSMarena" scraper.
"""
# GOOGLE_SEARCH = 'https://www.google.com/search?q='
MAIN_SITE = 'https://www.gsmarena.com'
SEARCH_PAGE = '/search.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
RESULTS_PAGE = '/results.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
BRANDS = {'Samsung': 9, 'Apple': 48}
APPLE = '48' # Makerid
SAMSUNG = '9' # Makerid
AVAILABLE = '1,3' # 1 - Available, 3 - Discontinued
FORM_FACTOR = '1'  # 1 - Bar
YEAR_RANGE = range(2009, 2022)
# &nbsp  - HTML entity which indicate " space that will not break into a new line"
# https://www.w3schools.com/html/html_entities.asp
NON_BREAK_SPACE = u'\xa0'
REQUEST_BATCH_DELAY = 60  # seconds
BATCH_SIZE = 10
REQUEST_SINGLE_DELAY = 1

# REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
#                                 ' Gecko/20100101 Firefox/47.0'}
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0'}
# test
# print(MAIN_SITE + RESULTS_PAGE.format(2009, 2009, APPLE, AVAILABLE, FORM_FACTOR))

# request parameters
# https://realpython.com/python-requests/#other-http-methods
# more issues:
# https://stackoverflow.com/questions/47397919/python-requests-with-httpadapter-is-halting-for-hours
# https://docs.python-requests.org/en/master/user/advanced/
GSMARENA_MAX_RETRIES = 3  # number of retry the same request before raise ConnectionError
GSMARENA_TIMEOUT = 3  # number of seconds to wait on a response before timing out

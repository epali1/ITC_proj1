"""
This is config file for "GSMarena" scraper.
"""
MAIN_SITE = 'https://www.gsmarena.com'
RESULTS_PAGE = '/results.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
# WebSite codes:
# Maker id:      {'Samsung': 9, 'Apple': 48}
# Availability:  1 - Available, 3 - Discontinued
# Form Factor:   1 - Bar
BRANDS = {'Samsung': 9, 'Apple': 48}
AVAILABLE = '1,3'
FORM_FACTOR = '1'
YEAR_RANGE = range(2009, 2022)
# &nbsp  - HTML entity which indicate " space that will not break into a new line"
NON_BREAK_SPACE = u'\xa0'
# send request header to fool bot detectors
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0'}
# request parameters
REQUEST_DELAY = 3
GSMARENA_MAX_RETRIES = 3  # number of retry the same request before raise ConnectionError
GSMARENA_TIMEOUT = 3  # number of seconds to wait on a response before timing out

JSON_INDENT = 4

# logging params
LOG_NAME = "SmartPhoneScraper"
LOG_FILE = 'scraper.log'
LOG_CONSOLE_FORMAT = '%(name)s - %(levelname)s - %(message)s'
LOG_FILE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LVL = {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}

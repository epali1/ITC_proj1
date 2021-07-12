"""
This is config file for "GSMarena" scraper.
"""

MAIN_SITE = 'https://www.gsmarena.com'
SEARCH_PAGE = '/search.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
RESULTS_PAGE = '/results.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
APPLE = '48' # Makerid
SAMSUNG = '9' # Makerid
AVAILABLE = '1,3' # 1 - Available, 3 - Discontinued
FORM_FACTOR = '1'  # 1 - Bar
YEAR_RANGE = range(2009, 2022)
# &nbsp  - HTML entity which indicate " space that will not break into a new line"
# https://www.w3schools.com/html/html_entities.asp
NON_BREAK_SPACE = u'\xa0'

# test
print(MAIN_SITE + RESULTS_PAGE.format(2009, 2009, APPLE, AVAILABLE, FORM_FACTOR))
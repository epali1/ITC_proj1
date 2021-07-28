"""
This is config file for "GSMarena" scraper.
"""
MAIN_SITE = 'https://www.gsmarena.com'
SEARCH_PAGE = '/search.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
RESULTS_PAGE = '/results.php3?nYearMin={}&nYearMax={}&sMakers={}&sAvailabilities={}&sFormFactors={}'
BRANDS = {'Samsung': 9, 'Apple': 48}
# APPLE = '48' # Maker id
# SAMSUNG = '9' # Maker id
AVAILABLE = '1,3' # 1 - Available, 3 - Discontinued
FORM_FACTOR = '1'  # 1 - Bar
YEAR_RANGE = range(2009, 2022)
# &nbsp  - HTML entity which indicate " space that will not break into a new line"
# https://www.w3schools.com/html/html_entities.asp
NON_BREAK_SPACE = u'\xa0'

# send request header to fool not detectors
# https://stackoverflow.com/questions/47956527/how-do-websites-detect-bots
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox
# https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python
# https://hacks.mozilla.org/2013/09/user-agent-detection-history-and-checklist/
# REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
#                                 ' Gecko/20100101 Firefox/47.0'}
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0'}

# request parameters
# https://realpython.com/python-requests/#other-http-methods
# more issues:
# https://stackoverflow.com/questions/47397919/python-requests-with-httpadapter-is-halting-for-hours
# https://docs.python-requests.org/en/master/user/advanced/
REQUEST_DELAY = 3
GSMARENA_MAX_RETRIES = 3  # number of retry the same request before raise ConnectionError
GSMARENA_TIMEOUT = 3  # number of seconds to wait on a response before timing out


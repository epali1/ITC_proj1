"""
This is command line interface program to smartphone scrapper.
"""
import argparse
from datetime import datetime
from phone_scraper import *
from gsmarena_conf import *

DESC = """-------------SmartPhone Scraper-----------------"""
USAGE = """A command line interface program to smartphone scrapper.
This program scrape http://www.gsmarena.com smartphones properties.

    Examples:
        phone_scraper_cli.py  --brand=Apple --year_min=2011 --year_max=2015
        phone_scraper_cli.py  --brand=Samsung --year_max=2012 --outfile=phone_data.json
        phone_scraper_cli.py  --year_max=2012 --outfile=phone_data.json
        phone_scraper_cli.py  --log_lvl=DEBUG --logoff --logfile=scarper.log 
"""


def cli() -> argparse.Namespace:
    """
    command line function for phone_scraper.py
    """
    current_year = datetime.now().year

    parser = argparse.ArgumentParser(description=DESC, usage=USAGE)

    # Scraping Options
    parser.add_argument('--brand', type=str.capitalize, choices=['Apple', 'Samsung', 'All', 'None'], default='All')
    parser.add_argument('--year_min', type=int, default=2009,
                        help=f'Minimal search range (year_min>={YEAR_MIN})')
    parser.add_argument('--year_max', type=int, default=current_year,
                        help=f'Maximal search range (year_min>=year_max>{current_year})')
    parser.add_argument('--outfile', type=str, default='smartphone_data.json',
                        help='Output suffix file name.')

    # Logging Options
    parser.add_argument('--log_lvl',  choices=['DEBUG', 'INFO', 'WARNING'], default='INFO')
    parser.add_argument('--logfile', type=str, default=LOG_FILE,
                        help='Log file name. set None to disable log file.')
    parser.add_argument('--logoff', action='store_true', default=False,
                        help='Disable stdout logging.')

    # DataBase Options
    parser.add_argument('--DB',type=str.lower, choices=['new', 'update', 'del'], default='update')

    args = parser.parse_args()

    if args.year_min < YEAR_MIN:
        print("Warning: year_min can't be lower than 2009")
        parser.print_help()
        exit(1)
    elif args.year_min > current_year:
        print(f"Warning: year_min can't be higher than {current_year}")
        parser.print_help()
        exit(1)
    elif args.year_max < args.year_min:
        print("Warning: year_max can't be lower than year_min")
        args.year_max = args.year_min
        print(f"        change year_max value to: {args.year_max}")
    elif args.year_max > current_year:
        print("Warning: year_max can't be higher than current year")
        args.year_max = current_year
        print(f"        change year_max value to: {args.year_max}")

    return args


def check_brand_input(brands: list[str]) -> list[str]:
    """
    check user brand input
    input: brand as a list -> [brand]
    """
    if brands[0] == 'All':
        brands = ['Apple', 'Samsung']
    elif brands[0] is None:
        print('No brand name is given -- existing...')
        exit(0)

    return brands


def check_db_input(db_opt: str):
    """
    check user DB input
    """
    if db_opt == 'del':
        print('remove database data')
        exit(0)
    elif db_opt == 'new':
        print('remove database data if exist')
        print('continue and assume database update parameter is given')


def main():

    args = cli()
    print(vars(args))
    activate_log(log_lvl=args.log_lvl, logfile=args.logfile, logoff=args.logoff)

    brands = check_brand_input([args.brand])
    check_db_input(args.DB)

    for brand in brands:
        phones_data = smartphones_scraper(brand=brand, year_min=args.year_min, year_max=args.year_max)
        save_data(f'{brand}_{args.outfile}', phones_data)


if __name__ == "__main__":
    main()

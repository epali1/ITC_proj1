# ITC Data-Mining Project

## About
Smartphone-scraper is part 1 of ITC data-mining project

This program scrape "GSMarena.com" website for smartphone data
Scraping is limited to:
* Apple and Samsung smartphone only
* from 2009 only
* only Bar (type) smartphones

Output results save into a json files

## Requirements

python==3.9.5  
requests==2.25.1
beautifulsoup4==4.9.3
pytest==6.2.4
bs4==4.9.3
pymysql=1.0.2

## Installation

1. Clone the repository to your computer

```bash
$ git clone  https://github.com/epali1/ITC_proj1.git
```

2. Create a python new environment and install the requirements  
   1. [using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

      create new environment with python 3.9.5   
      note: "my_env" can be the name of your choosing   
      (windows)
       ```bash
      $ py -m venv my_env
      ```
      (linux)
       ```bash
      $ python3 -m venv my_env
      ```
      
      activate the environment  
      (windows)
      ```bash
      $ .\my_env\Scripts\activate
      ```
      (linux)
      ```bash
      $ source my_env/bin/activate
      ```
            
      install the requirements
      
      ```bash
      $ pip install -r requirements.txt 
      ```

   2. [using conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

      create new environment with python 3.9.5
      
      ```bash
      $ conda create --name my_env python=3.9.5
      ```
      activate the environment 

      ```bash
      $ conda activate my_env 
      ```
      install the requirements

      ```bash
      $ conda install --file requirements.txt
      ```
      
## Usage

use phone-scraper_cli.py   
examples:    

1. Scrape 'Apple' smartphones data from 2011 to 2015. The data will save at default file 'Apple_smartphones_data.json'.
```bash
$ phone_scraper_cli.py  --brand=Apple --year_min=2011 --year_max=2015
```

2. Scrape 'Samsung' smartphones data from 2012 to current year. The data will save at default file 'Samsung_phone_data.json'.
```bash
$ phone_scraper_cli.py  --brand=Samsung --year_min=2012 --outfile=phone_data.json
```
        
3. Scrape 'Samsung' and 'Apple' smartphones data from 2009 to 2012. The data will save at default file 'Apple_phone_data.json' and 'Samsung_phone_data.json'.
```bash
$ phone_scraper_cli.py  --year_max=2012 --outfile=phone_data.json
```

4. Log options. 
```bash
$ phone_scraper_cli.py  --log_lvl=DEBUG --logoff --logfile=scarper.log 
```

5. DB options. remove existing database, scrape and save the data in a new database file.
```bash
$ phone_scraper_cli.py  --year_max=2012 --DB=new  
```

6. DB options. remove existing database, do nothing else.
```bash
$ phone_scraper_cli.py  --DB=del  
```

7. DB options. update database (default). Ignore existing data.
```bash
$ phone_scraper_cli.py  --year_min=2012 --DB=update  
```

## cli option

|  option  |         description        |               values               |
|:--------:|:--------------------------:|:----------------------------------:|
|   brand  |  choose smartphones brand  | ['Apple', Samsung', 'All', 'None'] |
| year_min |  year start scraping from  |            2009-currnet            |
| year_max |    year end scraping to    |          year_min-current          |
|  outfile |    suffix to output file   |    'brand'_smartphones_data.json   |
|  log_lvl |      global log level      |    ['WARNING', 'INFO', 'DEBUG']    |
|  logfile |          log file          |  empty string to disable log file  |
|  logoff  | disable log console output |               boolean              |
|  DB      |          DB option         |     ['new', 'update', 'delete']    |


## testing

for testing, run pytest in the project directory
```bash
$ pytest -v 
```

## Convention
The code is PEP8 Compliant

## Contributors
Samuel Abettan,  
Yair Ben-Shaul
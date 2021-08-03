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
bs4==4.9.3  
pytest==6.2.4

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

run phone-scraper.py 
```bash
$ phone-scraper.py
```
The result will be stored at: 
- apple_smartphones_data.json
- samsung_smartphone_data.json

for testing, run pytest in the project directory
```bash
$ pytest -v 
```

## Convention
The code is PEP8 Compliant

## Contributors
Samuel Abettan,  
Yair Ben-Shaul

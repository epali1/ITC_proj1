# ITC Data-Mining Project.

## About
smartphone-scraper is part 1 of ITC data-mining project.

This program scrape "GSMarena.com" website for smartphone data.
Scarping is limited to:
* Apple and Samsung smartphone only.
* from 2009 only.
* only Bar (type) smartphones.

Output results save into a json files.

## requirements

python >= 3.9.5  
requests >=   
bs4 >=  

## Instalation

1. clone the repository to your computer.

```bash
git clone  https://github.com/epali1/ITC_proj1.git
```

2. create a python new envirement and install the requirements  
   1. [using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

      note: "my_env" can be the name of your choosing.

       ```bash
      py -m venv my_env
      .\my_env\Scripts\activate
      ```

      ```bash
      pip install -r requirements.txt 
      ```

   2. [using conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

      ```bash
      conda create --name my_env python=>3.9.5
      ```

      ```bash
      conda activate my_new_env 
      ```

      ```bash
      conda install < requirements.txt
      ```
      
## Useage

just run phone-scraper.py 
```bash
$ phone-scraper.py
```
The result will be save at: 
- apple_smartphones_data.json
- samsung_smartphone_data.json

## Contributors
Samuel Abettan,  
Yair Ben-Shaul

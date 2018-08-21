# Crawler Challenge

The purpose of this code is to create a crawler that visits the site epocacosmeticos.com.br and save a .csv file with the product name, title and url of each product page found.

Rules:
 
 - This file should not contain duplicate entries;
 - It is not allowed to use the sitemap to get all urls from the site; the site must in fact be visited and parsed to obtain the information;
 - Except for Scrapy, you can use the frameworks and libraries you want, as long as the main language used is Python;
 
 
# Required
 - Python 3
 
# How to install

 1. clone the repository.
 2. create a virtualenv with Python 3.5. (https://virtualenv.pypa.io/en/stable/)
 3. activate virtualenv.
 4. install the dependencies. (pip install -r requirements.txt)
 5. run the project.
 
 ```console
 git clone git@github.com:lffsantos/captura.git
 cd captura
 virtualenv -p python3 .virtualenv
 source .virtualenv/bin/activate
 pip install -r requirements.txt
 make run
```

# How to Run:

 - Install Requirements and the Application;  
	pip install -r requirements.txt
 
 - Create Application Database;
	python core/db/database.py
 
 - Rotate Crawler;  
	python core/modules/crawler.py
        
- Rotating the Processor;
	python core/modules/processor.py

- Rotate Indexer:
	python core/modules/indexer.py

- Using Makefile
	
```console
make run
```

## Módulos (core/modules) 
 
### crawler.py
   - Responsável por capturar os links da url informada.  
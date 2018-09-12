# Web Crawler

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
 git clone https://github.com/asafepy/crawler-challenge.git
 cd crawler-challenge
 virtualenv -p python3 .virtualenv
 source .virtualenv/bin/activate
 pip install -r requirements.txt
 make install
 make run
```

# How to Run:

1. Install Requirements and the Application;  
	- pip install -r requirements.txt
 
2. Create Application Database;
	- python core/db/database.py
 
3. Rotate Crawler;  
	- python core/modules/crawler.py
        
4. Rotating the Processor;
	- python core/modules/processor.py

5. Rotate Indexer:
	- python core/modules/indexer.py

7. Using Makefile
	
```console
make run
```

## Modules (core/modules) 
 
### crawler.py (MultiThread)
- Responsible for capturing links from the url informed.



### processor.py (Multiprocess)
- Responsible for reading the raw information in the database (WAIT) and updating it.
- This is a multiprocess application, you can keep running in the background and you can upload as many applications as you want, you can add more machines and / or more processes to increase the processing speed.


### indexer.py (SingleProcess)
- Responsible for generating the csv file, queries the database for all records processed and indexes in a csv worksheet.
- The indexer can be rotated whenever you want, refreshing the spreadsheet data. if you do not have new data that has been processed nothing will be indexed. But if the processor has consumed new messages and updated information the worksheet will be updated with these new values.

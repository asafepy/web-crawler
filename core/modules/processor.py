import argparse
import concurrent.futures
import json
import re
from multiprocessing import Process

from core.db.database import get_engine_db
from core.db.products import Product_db
from core.utils.parser import Parser
from core.modules.crawler import Crawler

__author__ = 'asafe'


class Processor(object):
    _test = False

    @classmethod
    def get_urls(self):
        product_db = Product_db(get_engine_db(self._test))
        products = product_db.get_products_for_status('WAIT')
        return products

    @classmethod
    def parser_and_update(self, key, url):

        content = Parser(url)
        Product_db(get_engine_db(self._test)).update_product(
            key, content.get_title(), content.get_name(), 'PROCESSED'
        )

    @classmethod
    def validate_url(self, url):
    
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ... ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        return re.match(regex, url)


    
if __name__ == "__main__":

    processor = Processor()

    def multiprocessed():
        
        processes = []
        
        for product in processor.get_urls():
            if processor.validate_url(product.url):
                process = Process(target=processor.parser_and_update, args=(product.id, product.url))
                processes.append(process)

        for p in processes:
            p.start()
        
        for p in processes:
            p.join()


    multiprocessed()
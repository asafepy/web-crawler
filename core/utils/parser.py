import requests

from bs4 import BeautifulSoup


class Parser(object):

    def __init__(self, url):
    	self.url = url
        self.session = requests.Session()
        html = self.session.get(url)
        self.content_page = BeautifulSoup(html.content, "html.parser")

        self.regex = re.compile(
	        r'^(?:http|ftp)s?://' # http:// or https://
	        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	        r'localhost|' #localhost...
	        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	        r'(?::\d+)?' # optional port
	        r'(?:/?|[/?]\S+)$', re.IGNORECASE
	    )

    def get_title(self):
        return self.content_page.title.string

    def get_name(self):
        tag = self.content_page.find_all("div", class_="productName")[0]
        return tag.string

    def validate_url(self):
    	return re.match(self.regex, self.url)
# print  is not None   # True
# print re.match(regex, "example.com") is not None         
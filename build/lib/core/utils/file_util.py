import csv
import os

__author__ = 'asafe'


def has_header(file, header):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if list(row) != header:
                raise ValueError('invalid header')

            return True


def add_header(file, header):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)


def create_file(file, header):
    if not os.path.exists(file):
        add_header(file, header)
    else:
        if not has_header(file, header):
            add_header(file, header)

def validate_url(self, url):    
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    return re.match(regex, url)
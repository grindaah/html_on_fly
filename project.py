#coding utf-8
import sys
sys.path.append("./html_lib")

from html_lib import urler
from html_lib import sqler
from html_lib import htmler

from sys import argv

sample = "http://localhost:8000/products"
def __main__(options):
    if len(options) > 1:
        print "Some useless data, only one paramater needed"

    print options
    path, req, param, label = urler.urler(options[0])
    page_data, page_name = sqler.perform_request("my_first_db.sqlite", req)
    htmler.htmler(page_data, page_name)

if __name__ == '__main__':
    if len(argv) > 1:
        __main__(argv[1:])
    else:
        __main__([sample])

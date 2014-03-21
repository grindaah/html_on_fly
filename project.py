#coding utf-8
import html_lib
#import "html_lib/urler.py"
sample = "http://localhost:8000/products"
def __main__(options):
    if len(options) > 1:
        print "Some useless data, only one paramater needed"

    req, param, label = urler.urler(options[0])
    page_data, page_name = sql_getter.perform_request("my_first_db.sqlite", req)
    htmler.htmler(page_data, page_name)

if __name__ == 'main':
    main(argv[1:])

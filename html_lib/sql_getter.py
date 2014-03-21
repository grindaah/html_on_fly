import sqlite3

filename = 'my_first_db.sqlite'

def perform_request(base, request, params):
    conn = sqlite3.connect(base)
    c = conn.cursor()
    if len(params
    str_ = "SELECT * FROM %s WHERE %s" % (request, params)

    try:
        c.execute(str_)
    except OperationError:
        print str_ , "can not be parsed"

    rows = c.fetchall()
    print rows
    return rows, request


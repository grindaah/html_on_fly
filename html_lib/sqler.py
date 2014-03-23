#coding: utf-8
import sqlite3

filename = 'my_first_db.sqlite'

def perform_request(base, request, params="1"):
    conn = sqlite3.connect(base)
    c = conn.cursor()
    str_ = "SELECT * FROM %s WHERE %s" % (request, params)

    try:
        c.execute(str_)
    except OperationError:
        print str_ , "can not be parsed"

    rows = c.fetchall()
    print rows
    return rows, request

def add_row(Id, name, Price):
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    try:
        c.execute("INSERT INTO products VALUES ({id}, '{Name}', {price})".format(id = Id, Name = name, price = Price))
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_second))

    conn.commit()
    conn.close()

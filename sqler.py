import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'clients'  # name of the table to be created
table_name2 = 'products'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_types = ['INTEGER', 'BLOB', 'TEXT']  # column data type

table1_columns = ["Id", "Name"]
table2_columns = ["Id", "Name", "Price"]

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#def sql_add(no, name, price):
#    sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
#    conn = sqlite3.connect(sqlite_file)
#    c = conn.cursor()

   # str_ = "INSERT INTO products VALUES (%d, '%s', %d)" % (no, name, price)
 #   c.execute(str_)
  #  c.commit()
  #  c.close()

#sql_add(2, "airbus", 50000000)
#sql_add(3, "boeing", 30000000)

# Creating a new SQLite table with 1 column
#c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=new_field, ft=field_types[0]))
#c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name2, nf=new_field, ft=field_types[0]))

#c.execute("CREATE TABLE products (No INTEGER, Name TEXT, Price INTEGER)")
#c.execute("CREATE TABLE clients (No INTEGER, Name TEXT)")


#try:
   # c.execute("INSERT INTO products VALUES ('No'='1', 'Name'='screwdriver', 'Price'='14'), ('No'='2', 'Name'='laptop', 'Price'='10000'), ('No'='3', 'Name'='airbus', 'Price'='1000000')")
c.execute("INSERT INTO products VALUES (3, 'LT11',14000000)")
c.execute("INSERT INTO products VALUES (4, 'airbus',1400000)")
c.execute("INSERT INTO products VALUES (5, 'R2D2',14000000)")
#except sqlite3.IntegrityError:
#    print('ERROR: Id already exists in PRIMARY KEY column {}'.format(id_column))

#try:
#    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name1, idf=0, cn=column_name))
#except sqlite3.IntegrityError:
#    print('ERROR: Id already exists in PRIMARY KEY column {}'.format(id_column))



# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


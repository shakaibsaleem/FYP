# from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import *
import pandas as pd
import urllib

# Read file into a DataFrame and print its head
df = pd.read_csv('khaadi.csv')
# print(df.head())
# print(df)

# conString = "Data Source = .\\SQLEXPRESS;Initial Catalog = fyp; Persist Security Info=True;User ID = sa; Password=studio19;"

# conString = "mssql+pyodbc://sa:studio19@SQLEXPRESS/fyp"

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=.\\SQLEXPRESS;DATABASE=fyp;UID=sa;PWD=studio19")
conString = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(conString)

mytables = engine.table_names()

# print(tables)

metadata = MetaData()

# p = tables[4]
# print(p)

product_table = Table(mytables[4], metadata, autoload = True, autoload_with = engine)

# print(repr(product_table))
# print(repr(metadata.tables[mytables[4]]))

# print(product_table.columns.keys())

connection = engine.connect()

select_stmt = "select * from "

# ResultProxy
result_proxy = connection.execute(select_stmt + mytables[4])

# ResultSet
results = result_proxy.fetchall()

# print(product_table.columns.keys())
# print(results)
# print(results[0])
# print(type(results[0]['idProduct']))

# first_row = results[0]
# print(first_row.keys())
# print(first_row.idProduct)
# print(first_row['idProduct'])
# print(first_row)

select_new = select([product_table])
# print(select_new)
results_new = connection.execute(select_new).fetchall()
# print(results_new)

# staging table. new data in a temp table. procedure written there that updates. check lab of database about import/export data
# principal component analysis -> dimension reduction. 13 to 5. effective.
# pysom library. self organising maps for python

select_where = select_new.where(product_table.columns.PCode == 'code')
results_where = connection.execute(select_where).fetchall()
# print(results_where)

df2 = pd.DataFrame(results_where)
df2.columns = results_where[0].keys()
print(df2)


'''
# Import insert and select from sqlalchemy
from sqlalchemy import insert, select

# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name="Anna", count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results
results = connection.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == "Anna")

# Print the result of executing the query.
print(connection.execute(stmt).first())







# Build a list of dictionaries: values_list
values_list = [
    {'name': "Anna", 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': "Taylor", 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
'''


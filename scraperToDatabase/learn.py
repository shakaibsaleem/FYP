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
print(results_new)

# staging table. new data in a temp table. procedure written there that updates. check lab of database about import/export data
# principal component analysis -> dimention reduction. 13 to 5. effective.
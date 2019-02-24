from sqlalchemy import *
import pandas as pd
import urllib

df = pd.read_csv('khaadi.csv')

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=.\\SQLEXPRESS;DATABASE=fyp;UID=sa;PWD=studio19")
conString = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(conString)
mytables = engine.table_names()

metadata = MetaData()
product_table = Table(mytables[4], metadata, autoload = True, autoload_with = engine)

# print(product_table.columns.keys())

connection = engine.connect()

select_stmt = "select * from "

result_proxy = connection.execute(select_stmt + mytables[4])

# result_set = result_proxy.fetchall()

results = pd.DataFrame(result_proxy.fetchall())
results.columns = result_proxy.keys()

# print(result_set)

print(results)
print()
print(df.columns)
print()
print("done")
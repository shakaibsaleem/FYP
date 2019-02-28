from sqlalchemy import *
import pandas as pd
import urllib

df = pd.read_csv('khaadi.csv')


params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=.\\SQLEXPRESS;DATABASE=fyp;UID=sa;PWD=uiop7890")
conString = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(conString)
mytables = engine.table_names()

metadata = MetaData()
product_table = Table(mytables[4], metadata, autoload = True, autoload_with = engine)
# print(mytables)
# print(product_table.columns.keys())

connection = engine.connect()

select_stmt = "select * from "

result_proxy = connection.execute(select_stmt + mytables[4])
# print(mytables)
results = pd.DataFrame(result_proxy.fetchall())
results.columns = result_proxy.keys()

CategoryTablep = connection.execute(select_stmt + mytables[0])
CategoryTable = pd.DataFrame(CategoryTablep.fetchall()).set_index(0)

MaterialTablep = connection.execute(select_stmt + mytables[3])
MaterialTable = pd.DataFrame(MaterialTablep.fetchall()).set_index(0)

colorTablep = connection.execute(select_stmt + mytables[1])
colorTable = pd.DataFrame(colorTablep.fetchall()).set_index(0)

WebsiteTablep = connection.execute(select_stmt + mytables[-1])
WebsiteTable = pd.DataFrame(WebsiteTablep.fetchall()).set_index(0)


for x,y in df.iterrows():
	a = df.at[x,'Dress Code']
	b = (results[(results == a).any(1)].stack()[lambda x: x != a])
	listOfAtributes = (list(b))
	if listOfAtributes != []:
		if colorTable.at[(listOfAtributes[3]) , 1] == df.at[x,'Color']:
			print('color sahi')
		if str(CategoryTable.at[listOfAtributes[1] , 1]) == str(df.at[x,'Category']):
			print('category sahi')
		if (MaterialTable.at[listOfAtributes[2] , 1]) == df.at[x,'Material']:
			print('material sahi')
		if (WebsiteTable.at[listOfAtributes[4],1]) == df.at[x,'Brand']:
			print('website sahi')
		if df.at[x,'Name'].split(' ')[0] == (listOfAtributes[5]).split(' ')[0]:
			print('name sahi')
		if int(df.at[x,'Price']) == int(listOfAtributes[6]):
			print('price sahi')
		if df.at[x, 'url'] == listOfAtributes[7]:
			print('url sahi')
		if df.at[x,'Description'] == listOfAtributes[-1]:
			print('description sahi')

	# if df.at[x,'']
	# print(results.at[x,'PCode'])

# for x,y in df.iterrows():
# 	print(df.at[x,'Dress Code'])

# print(type(results))
# print()
# print(df.columns)
# print()
print("done")
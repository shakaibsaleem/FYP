from sqlalchemy import *
import pandas as pd
import urllib

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=.\\SQLEXPRESS;DATABASE=fyp;UID=sa;PWD=uiop7890")
conString = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(conString)
mytables = engine.table_names()

metadata = MetaData()
print(metadata)
product_table = Table(mytables[4], metadata, autoload = True, autoload_with = engine)

connection = engine.connect()

def updateColor(color, PCode):
	updatequery = "update Product set idColor = (select idColor from Color where Color =" + str(color) + ') where idProduct = (select idProduct from Product where PName = ' + str(PCode) + ')' 
	connection.execute(updatequery)

def insertColor(color):
	query = "insert into Color values ('" + str(color) + "')"
	connection.execute(query)

def updateCategory(category, PCode):
	updatequery = "update Product set idCategory = (select idCategory from Color where Category =" + str(category) + ') where idProduct = (select idProduct from Product where PName = ' + str(PCode) + ')' 
	connection.execute(updatequery)

def insertCategory(category):
	query = "insert into Category values ('" + str(category) + "')"
	connection.execute(query)

def updateMaterial(Material, PCode):
	updatequery = "update Product set idMaterial = (select idMaterial from Material where Material =" + str(Material) + ') where idProduct = (select idProduct from Product where PName = ' + str(PCode) + ')' 
	connection.execute(updatequery)

def insertMaterial(Material):
	query = "insert into Material values ('" + str(Material) + "')"
	connection.execute(query)

def insertWebsite(Website,webpage):
	query = "insert into Website values ('" + str(Website) + "', '"+ webpage + "')"
	connection.execute(query)

def updateWebsite(Website, PCode):
	updatequery = "update Product set idWebsite = (select idWebsite from Website where WName =" + str(Website) + ') where idProduct = (select idProduct from Product where PName = ' + str(PCode) + ')' 
	connection.execute(updatequery)


def insertProduct(details):
	query = "insert into Product values ((select idCategory from Category where Category ='" + details[0] 
	query = query + "'),(select idMaterial from Material where Material ='" 
	query = query + details[1] + "'),(select idColor from Color where Color = '" + details[2] 
	query = query + "'),(select idWebsite from Website where WName = '" + details[3] + "'),'"
	query = query + details[4].strip() + "'," + details[5] + ",'" + details[6] +"',"+ " 1, '"+ details[7] 
	query = query + "','"+details[8]
	query = query + "')"
	print(query)
	connection.execute(query)


def main():
	df = pd.read_csv('khaadi.csv')


	select_stmt = "select * from "

	result_proxy = connection.execute(select_stmt + mytables[4])
	# print(mytables)
	results = pd.DataFrame(result_proxy.fetchall())
	# results.columns = result_proxy.keys()
	try:
		CategoryTablep = connection.execute(select_stmt + mytables[0])
		CategoryTable = pd.DataFrame(CategoryTablep.fetchall()).set_index(0)
	except:
		pass

	try:
		MaterialTablep = connection.execute(select_stmt + mytables[3])
		MaterialTable = pd.DataFrame(MaterialTablep.fetchall()).set_index(0)
	except:
		pass

	try:
		colorTablep = connection.execute(select_stmt + mytables[1])
		colorTable = pd.DataFrame(colorTablep.fetchall()).set_index(0)
	except:
		pass
	try:
		WebsiteTablep = connection.execute(select_stmt + mytables[-1])
		WebsiteTable = pd.DataFrame(WebsiteTablep.fetchall()).set_index(0)
	except:
		pass
	for x,y in df.iterrows():
		a = df.at[x,'Dress Code']
		# print(results)
		b = (results[(results == a).any(1)].stack()[lambda x: x != a])
		listOfAtributes = (list(b))
		if listOfAtributes != []:
			if colorTable.at[(listOfAtributes[3]) , 1] == df.at[x,'Color']:
				print('color sahi')
			else:
				if df.at[x,'Color'] not in colorTable.unique():
					insertColor(df.at[x,'Color'])
					updateColor(df.at[x,'Color'],str(a))
				else:
					updateColor(df.at[x,'Color'],str(a))
			if str(CategoryTable.at[listOfAtributes[1] , 1]) == str(df.at[x,'Category']):
				print('category sahi')
			else:
				if df.at[x,'Category'] not in CategoryTable.unique():
					insertCategory(df.at[x,'Category'])
					updateCategory(df.at[x,'Category'],str(a))
				else:
					updateCategory(df.at[x,'Category'],str(a))
			if (MaterialTable.at[listOfAtributes[2] , 1]) == df.at[x,'Material']:
				print('material sahi')
			else:
				if df.at[x,'Material'] not in MaterialTable.unique():
					insertMaterial(df.at[x,'Material'])
					updateMaterial(df.at[x,'Material'],str(a))
				else:
					updateMaterial(df.at[x,'Material'],str(a))
			if (WebsiteTable.at[listOfAtributes[4],1]) == df.at[x,'Brand']:
				print('website sahi')
			else:
				if df.at[x,'Brand'] not in (WebsiteTable.values):
					if df.at[x,'Brand'] == ['Khaadi']:
						insertWebsite(df.at[x,'Brand'],'https://www.khaadi.com/pk/')
					elif df.at[x,'Brand'] == ['Zellbury']:
						insertWebsite(df.at[x,'Brand'],'https://www.Zellbury.com')
				else:
					updateWebsite(df.at[x,'Website'],str(a))

			if df.at[x,'Name'].split(' ')[0] == (listOfAtributes[5]).split(' ')[0]:
				print('name sahi')
			if int(df.at[x,'Price']) == int(listOfAtributes[6]):
	 			print('price sahi')
			if df.at[x, 'url'] == listOfAtributes[7]:
				print('url sahi')
			if df.at[x,'Description'] == listOfAtributes[-1]:
				print('description sahi')
		else:
			if df.at[x,'Color'] not in (colorTable.values):
					insertColor(df.at[x,'Color'])
					colorTablep = connection.execute(select_stmt + mytables[1])
					colorTable = pd.DataFrame(colorTablep.fetchall()).set_index(0)

			# if df.at[x,'Material'] == ['nan']:
			# 		pass
			if df.at[x,'Material'] not in (MaterialTable.values):
					print(df.at[x,'Material'])
					insertMaterial(df.at[x,'Material'])
					MaterialTablep = connection.execute(select_stmt + mytables[3])
					MaterialTable = pd.DataFrame(MaterialTablep.fetchall()).set_index(0)
					
			if df.at[x,'Category'] not in (CategoryTable.values):
					insertCategory(df.at[x,'Category'])
					CategoryTablep = connection.execute(select_stmt + mytables[0])
					CategoryTable = pd.DataFrame(CategoryTablep.fetchall()).set_index(0)

			if df.at[x,'Brand'] not in (WebsiteTable.values):
				if df.at[x,'Brand'] == ['Khaadi']:
					insertWebsite(df.at[x,'Brand'],'https://www.khaadi.com/pk/')
				elif df.at[x,'Brand'] == ['Zellbury']:
					insertWebsite(df.at[x,'Brand'],'https://www.Zellbury.com')	
				
				WebsiteTablep = connection.execute(select_stmt + mytables[-1])
				WebsiteTable = pd.DataFrame(WebsiteTablep.fetchall()).set_index(0)
					
			# print('x',x)
			listofValues = [str(df.at[x,'Category']),str(df.at[x,'Material']),str(df.at[x,'Color']),str(df.at[x,'Brand']),str(df.at[x,'Name']),str((df.at[x,'Price'])),str(df.at[x, 'url']),str(df.at[x,'Dress Code']),df.at[x,'Description']]
			print(listofValues)
			insertProduct(listofValues)
			result_proxy = connection.execute(select_stmt + mytables[4])
			results = pd.DataFrame(result_proxy.fetchall())
			results.columns = result_proxy.keys()

	# print()
	print("done")


main()
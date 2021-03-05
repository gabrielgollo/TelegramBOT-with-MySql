import mysql.connector

class MyDatabase:
	def __init__(self, fhost="localhost", fuser="root", fpassword="admin", fdatabase="telegram_bot"):
		self.connected=False
		try:
			self.mydb = mysql.connector.connect(
			host=fhost,
			user=fuser,
			password=fpassword,
			database=fdatabase)
			self.mycursor = self.mydb.cursor()
			self.connected=True
		except mysql.connector.InterfaceError:
			self.connected=False

	def imprimir(self):
		print(self.mydb)

	def showDatabases(self):
		self.mycursor.execute("SHOW DATABASES")

		myresult = self.mycursor.fetchall()
		return myresult

	def createDatabase(self, databasename):
		values=(databasename, )
		self.mycursor.execute("CREATE DATABASE %s", values)
		self.mydb.commit()

	def insertMsg(self, keyanswer, answer):
		sqlcode = "INSERT INTO `dicionario`(`key-answer`, `answer`) VALUES (%s, %s)"
		values = (keyanswer, answer)
		try:
			self.mycursor.execute(sqlcode, values)
			print("Success into insert MSG: " + values[1])
		except mysql.connector.errors.IntegrityError:
			pass
		self.mydb.commit()

	def removeMsg(self, keyanswer=''):
		if(len(keyanswer)<1):
			return
		sqlcode= "DELETE FROM `dicionario` WHERE `key-answer`=%s"
		values=(keyanswer, )
		try:
			self.mycursor.execute(sqlcode, values)
			self.mydb.commit()
			return "OK"
		except mysql.connector.IntegrityError:
			return "Integrity Error"

	def searchMsg(self, searchkey, DBtable, DBcolumn, default_Column = "*"):
		sqlcode= "SELECT {} FROM {} WHERE `{}` LIKE %s".format(default_Column, DBtable,  DBcolumn)
		values = (searchkey, )
		try:
			self.mycursor.execute(sqlcode, values)
			myresult = self.mycursor.fetchall()
			#print(myresult)
		except (mysql.connector.errors.OperationalError, AttributeError):
			self.reconnect()
			return []
		try:
			return myresult
		except IndexError:
			return []

	def close(self):
		try:
			self.mydb.close()
		except AttributeError:
			return False

	def reconnect(self):
		self.__init__()


'''
database = MyDatabase()            ##INIT DB
#print(database.searchMsg("ola"))  ##SEARCH AND PRINT
#database.insertMsg("oi", "oi")    ##INSERT MSG
print(database.removeMsg())		   ##REMOVE MSG
database.close()				   ##CLOSE DB
'''

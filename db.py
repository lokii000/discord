import mysql.connector as db

#Saving Search command 
def save_search(search,user, id): 
	
	# connection with database
	mydb = db.connect(host="localhost",  user="username", passwd="password", database ="db_name") 
	mycursor = mydb.cursor()
	
	if(mydb):
		print("connected")
	else:
		print("connection Failed")
		
	
	# Saving  seach history into database
	
	sql = "insert into history(command, user ,user_id) values(%s, %s, %s)"
	val = (search, user, id)
	
	mycursor.execute(sql, val)
	
	mydb.commit()	
	mydb.close()
	

def get_search(search,id):
	
	# connection with database
	
	mydb = db.connect(host="localhost",  user="username", passwd="password", database ="db_name") 
	mycursor = mydb.cursor()
	
	if(mydb):
		print("connected")
	else:
		print("connection Failed")
	
	id = str(id)
	
	#getting search history requested by user
	
	sql = "SELECT command FROM `history` WHERE command LIKE '%"+search+"%'"
	
	results = mycursor.execute("SELECT command FROM `history` WHERE user_id = '"+id+"'and command LIKE '%"+search+"%'")  
	
	result = mycursor.fetchall()
	
	mydb.close()
	
	if(result):		
		return result
	else:
		print("query failed")
		return False
	
	
	
	
	
	
	
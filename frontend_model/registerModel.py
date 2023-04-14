from flask import session
import pymysql

def registermodel(registerinfo):
	#here is where we make the connection to the database and create the account
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
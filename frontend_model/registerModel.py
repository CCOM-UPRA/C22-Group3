from flask import session
import pymysql

def registermodel(registerinfo):
	#here is where we make the connection to the database and create the account
    inf = tuple(registerinfo)
    
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    #I need to add a row to the table customers with the 
    cur.execute("INSERT INTO customers (c_firstname, c_lastname, c_email, c_password, phonenum, street, city, state, zipcode, c_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'active')", inf)
    conn.commit()
    print(cur.rowcount, "record inserted.")
    cur.close()
    conn.close()

def email_already_in_usemodel(email):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()

    cur.execute("SELECT c_email FROM customers WHERE c_email = %s", (email,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        # Email is already in use
        return True
    else:
        # Email is not in use
        return False

    
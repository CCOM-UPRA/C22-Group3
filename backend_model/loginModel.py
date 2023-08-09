from flask import session
from backend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt


def loginmodel(email, password):
    # DB credentials found in backend_model/connectDB.py
    user = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * from admin WHERE a_email = %s", email)
    userFound = cur.fetchall()
    # Save user info in list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2],
                     "email": users[3], "password": users[4],
                     "status": users[5]})
    cur.close()
    conn.close()
    
    for u in user:
        #print("Hashed password from user: ", u['password'])
        if email == u['email'] and password == u['password']:
            session['admin'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
    return "false"



from flask import session
import pymysql
from passlib.hash import sha256_crypt

def loginmodel(email, password):

    # Receive email and password to check in the "database"

    user = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * from customers WHERE c_email = %s", email)
    userFound = cur.fetchall()
    # Save user info in list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6]})
    
    for u in user:
        #print("Hashed password from user: ", u['password'])
        if email == u['email'] and sha256_crypt.verify(password, u['password']):
            session['customer'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
    return "false"

from flask import session
import pymysql
from passlib.hash import sha256_crypt

def loginmodel(email, password):

    # Receive email and password to check in the "database"

    user = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE c_email = %s AND c_password = %s", (email,password))
    userFound = cur.fetchall()
    for users in userFound:
       # user.append({"id": users[0], "name": users[1], "last_name": users[2], "address_line1": users[3],
                   #"address_line2": users[4], "city": users[5], "state": users[6], "zipcode": users[7],
                    #"email": users[8], "password": users[9], "phone_number": users[10], "card_name": users[11],
                    #"card_type": users[12], "card_number": users[13], "exp_date": users[14], "status": users[15]})


            user.append({"id": users[0], "name": users[1], "last_name": users[2], "email": users[3],
                    "password": users[4], "phone_number": users[5], "street": users[6], "city": users[7], "state": users[8],
                    "zipcode": users[9], "status": users[10]})


    # Save user info in list

    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    #for u in user:
        #print("Hashed password from user: ", u['password'])
        #if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
          #  session['customers'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
          #  return "true"
        #else:
            # If it didn't find user
        #    return "false"
    for u in user:
        #print("Hashed password from user: ", u['password'])
        if email == u['email'] and password == u['password'] is True:
            session['customers'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"
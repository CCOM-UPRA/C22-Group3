import pymysql
from flask import session


def getUserModel():
    user = []
    # Connect to DB using given credentials
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    # Find user via the customer ID saved in session
    cur.execute("SELECT * from customers WHERE customer_id = %s", session['customer'])
    userFound = cur.fetchall()

    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6]})

    # To access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user


def editnumbermodel(number):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customers SET phonenum = %s WHERE customer_id = %s", (number, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


def editaddressmodel(aline1, aline2, state, zipcode, city):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customers SET street = %s, state = %s, city = %s,"
                    "c_state = %s, zipcode = %s WHERE customer_id = %s", (aline1, aline2, city, state, zipcode, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


def editpaymentmodel(name, c_type, number, exp_date):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET c_card_name = %s, c_card_number = %s, "
                    "c_card_type = %s, c_exp_date = %s WHERE c_id = %s",
                    (name, number, c_type, exp_date, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


def editprofilemodel(fname, lname, email):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET c_firstname = %s, c_lastname = %s, "
                    "email = %s WHERE customer_id = %s",
                    (fname, lname, email, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1

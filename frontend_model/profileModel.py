import pymysql
from flask import session


def getUserModel():
    user = []
    # Connect to DB using given credentials
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    # Find user via the customer ID saved in session
    query = """
    SELECT customer_id, c_firstname, c_lastname, c_email, c_password, phonenum, street, city, state, zipcode, c_status, card_num, p_brand, card_date_month, card_date_year
    FROM customers 
    NATURAL JOIN payment_info 
    WHERE customer_id = %s"""
    cur.execute(query, (session['customer'],))
    userFound = cur.fetchall()
    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6],
                     "card_number": users[11], "card_type": users[12], "cardmon": users[13], "cardyear": users[14],})

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


def editpaymentmodel(c_type, number, exp_mon, exp_year):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE payment_info SET p_brand = %s, card_num = %s, "
                    "card_date_month = %s, card_date_year = %s WHERE customer_id = %s",
                    (c_type, number, exp_mon, exp_year, session['customer']))
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
        cur.execute("UPDATE customers SET c_firstname = %s, c_lastname = %s, "
                    "c_email = %s WHERE customer_id = %s",
                    (fname, lname, email, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1

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
    SELECT customer_id, c_firstname, c_lastname, c_email, c_password, phonenum, street, city, state, zipcode, c_status
    FROM customers
    WHERE customer_id = %s"""
    cur.execute(query, (session['customer'],))
    userFound = cur.fetchall()
    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6],})

    # To access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user

def getPaymentModel():
    user = []
    # Connect to DB using given credentials
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    # Find user via the customer ID saved in session
    query = """SELECT payment_info.card_num, payment_info.p_brand, payment_info.card_date_month, payment_info.card_date_year, payment_info.zipcode
            FROM customers
            JOIN payment_info ON customers.customer_id = payment_info.customer_id
            WHERE customers.customer_id = %s;
            """
    cur.execute(query, (session['customer'],))
    userFound = cur.fetchall()
    # Save tuple information in a list
    for users in userFound:
        user.append({"card_number": users[0], "card_type": users[1], "cardmon": users[2], "cardyear": users[3], "p_zipcode": users[4]})

    if len(user) == 0:
        user = ["", "", "", "", ""]  

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


def editpaymentmodel(c_type, number, exp_mon, exp_year, p_zipcode):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    user = getPaymentModel()
    if (user == ["", "", "", "", ""] ):
        try:
            status = "active"
            cur.execute("INSERT INTO payment_info SET card_num = %s, card_date_month = %s, card_date_year = %s,"
                        "zipcode = %s, p_status = %s, p_brand = %s, customer_id = %s", (number, exp_mon, exp_year, p_zipcode, status, c_type, session['customer']))
            conn.commit()
            return 0

        except pymysql.Error as error:
            print(error)
            return 0

        else:
            cur.close()
            return 1
    else:
        try:
            status = "active"
            cur.execute("UPDATE payment_info SET card_num = %s, card_date_month = %s, card_date_year = %s,"
                        "zipcode = %s, p_status = %s, p_brand = %s WHERE customer_id = %s", (number, exp_mon, exp_year, p_zipcode, status, c_type, session['customer']))
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

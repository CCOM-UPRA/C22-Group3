from passlib.handlers.sha2_crypt import sha256_crypt
from flask import session
from frontend_model.profileModel import *


def getUser():
    return getUserModel()

def getPayment():
    return getPaymentModel()

def editnumbercontroller(number):
    return editnumbermodel(number)


def editaddresscontroller(street, state, zipcode, city):
    return editaddressmodel(street, state, zipcode, city)


def editpaymentcontroller(c_type, number, exp_mon, exp_year, p_zipcode):
    return editpaymentmodel(c_type, number, exp_mon, exp_year, p_zipcode)


def editprofilecontroller(fname, lname, email):
    return editprofilemodel(fname, lname, email)


def changePass(npassw, email):
    # Connect to MySQL database server using credentials provided
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)

    try:
        cur = conn.cursor()
        cur.execute("UPDATE customers SET c_password = %s WHERE c_email = %s AND customer_id = %s", (npassw, email, session['customer']))
        conn.commit()
        conn.close()
        cur.close()
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1



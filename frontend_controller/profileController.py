from passlib.handlers.sha2_crypt import sha256_crypt

from frontend_model.profileModel import *


def getUser():
    return getUserModel()


def editnumbercontroller(number):
    return editnumbermodel(number)


def editaddresscontroller(aline1, aline2, state, zipcode, city):
    return editaddressmodel(aline1, aline2, state, zipcode, city)


def editpaymentcontroller(name, c_type, number, exp_date):
    return editpaymentmodel(name, c_type, number, exp_date)


def editprofilecontroller(fname, lname, email):
    return editprofilemodel(fname, lname, email)


def changePass(npassw, email):
    user = []
    # Connect to MySQL database server using credentials provided
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    
    cur = conn.cursor()
    # Select the specific customer whose password you want to hash
    cur.execute("SELECT * from customer WHERE c_email = %s", (email,))
    userFound = cur.fetchall()

    # This part isn't necessary here but is shown so student can visualize the DB structure
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6]})
        # Save the user's password in 'passw'
        users[4] = npassw

    # Encrypt the password using the sha256_crypt function
    hash = sha256_crypt.encrypt(npassw)
    print("Hashed password: ", hash)

    try:
        # Once encrypted, save this new hashed password to DB
        cur.execute("UPDATE customer SET c_password = %s WHERE c_email = %s", (hash, email))
        conn.commit()
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1



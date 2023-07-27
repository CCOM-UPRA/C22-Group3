from flask import session
import pymysql

dictUser1 = {1: {'c_first_name': "Milena", 'c_last_name': "Ríos",
                'c_email': "milena.rios2@upr.edu", 'c_password': "aghetyeifc",
                'c_phone_number': 7871621782, 'c_status': 'active',
                'c_address_line_1': "Sector Barrios", 'c_address_line_2': "Calle 8 H20", 'c_city': "Hatillo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00612', 'c_card_name': 'Milena Rios', 'c_card_type': 'Visa', 'c_exp_date': '05-04-24',
                 'c_card_num': 1234123412341234}}

dictUser2 = {2: {'c_first_name': "Reina", 'c_last_name': "López",
                'c_email': "reina.lopez@upr.edu", 'c_password': "p1234567",
                'c_phone_number': 8981821728, 'c_status': 'active',
                'c_address_line_1': "Victor Azul", 'c_address_line_2': "Calle 9 A10", 'c_city': "Arecibo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00610', 'c_card_name': 'Reina Lopez', 'c_card_type': 'Discover', 'c_exp_date': '01-01-22',
                 'c_card_num': 1234123412341234}}

dictUser3 = {3: {'c_first_name': "Javier", 'c_last_name': "Quiñones",
                'c_email': "javier.quinones3@upr.edu", 'c_password': "pass1234",
                'c_phone_number': 7871231234, 'c_status': 'active',
                'c_address_line_1': "Vista Azulin", 'c_address_line_2': "Calle L11 L13", 'c_city': "Arecibor", 'c_state': "Puerto Ricor",
                 'c_zipcode': '00612', 'c_card_name': 'Javier Quiñones', 'c_card_type': 'Mastercard',
                 'c_exp_date': '01-01-23', 'c_card_num': 1234123412341234}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


userList = dictUser1
userList = MagerDicts(userList, dictUser2)
userList = MagerDicts(userList, dictUser3)


def getUserModel():
    admin_results = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                       user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT admin_id, a_firstname, a_lastname, a_email, a_status FROM admin WHERE admin_id = %s", (session['admin']))
    adminfound = cur.fetchone()

    if adminfound:
        admin_results = {"admin_id": adminfound[0], "fname": adminfound[1], "lname": adminfound[2], "email": adminfound[3], "status": adminfound[4]}

    cur.close()
    conn.close()

    return admin_results

def updateprofilemodel(fname, lname, email, status, aid):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()

    cur.execute("UPDATE admin SET a_firstname = %s, a_lastname = %s, a_email = %s, a_status = %s WHERE admin_id = %s;",(fname, lname, email, status, aid))
    conn.commit()
    
    cur.close()
    conn.close()

    return

def updatepasswordmodel(oldpass, pass1, adminid):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()

    cur.execute("UPDATE admin SET a_password = %s WHERE admin_id = %s;",(pass1, adminid))
    conn.commit()
    
    cur.close()
    conn.close()

    return
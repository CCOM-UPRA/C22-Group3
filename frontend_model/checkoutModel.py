import pymysql
from flask import session


def validateUserModel():
    user = []
    # Connect to DB using given credentials
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    # Find user via the customer ID saved in session
    query = """SELECT *
            FROM customers
            JOIN payment_info ON customers.customer_id = payment_info.customer_id
            WHERE customers.customer_id = %s;
            """
    cur.execute(query, (session['customer'],))
    userFound = cur.fetchall()
    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "city": users[7],
                     "state": users[8], "zipcode": users[9], "email": users[3], "password": users[4],
                     "phone_number": users[5], "status": users[10], "street": users[6],
                     "card_number": users[11], "cardmon": users[12], "cardyear": users[13], "p_zipcode": users[14],
                     "p_status": users[15], "p_brand": users[16],})
    if len(user) == 0:
        user = []
        new_user = {'p_brand': "", 'cardyear': "", 'cardmon': "", 'card_number': ""}
        user.append(new_user)
  

    return user

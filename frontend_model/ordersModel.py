import pymysql
from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

def getOrderModel():
    orderlist = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT tracking_number, price_total, day, order_id FROM orders NATURAL JOIN cont WHERE customer_id = %s;", session['customer'])
    results = cur.fetchall()
    for res in results:
        orderlist.append({"tracking": res[0], "total": res[1], "date": res[2], "o_id": res[3]})
    cur.close()
    conn.close()

    return orderlist

def getProductModel():
    productlist = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT s_name, image_link, s_brand, price, quantity FROM orders NATURAL JOIN cont NATURAL JOIN stickers WHERE customer_id = %s GROUP BY s_name", session['customer'])
    results = cur.fetchall()
    for res in results:
        productlist.append({"s_name": res[0], "img": res[1], "brand": res[2], "price": res[3], "quantity": res[4],})
    cur.close()
    conn.close()

    return productlist
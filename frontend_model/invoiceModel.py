import pymysql
from flask import session

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
    #cur.execute("SELECT MAX(order_id) from orders WHERE customer_id = %s", session['customer'])
    cur.execute("SELECT tracking_number, price_total FROM orders WHERE order_id = (SELECT MAX(order_id) FROM orders)AND customer_id = %s", session['customer'])
    results = cur.fetchall()
    for res in results:
        orderlist.append({"tracking": res[0], "total": res[1]})
    cur.close()
    conn.close()

    return orderlist


def getProductsModel():
    productlist = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM stickers NATURAL JOIN (SELECT sticker_id, quantity FROM cont WHERE order_id = (SELECT MAX(order_id) from orders WHERE customer_id = %s)) AS alias", session['customer'])
    results = cur.fetchall()
    for res in results:
        productlist.append({"id": res[0], "name": res[1], "brand": res[11], "desc": res[2],
                    "waterproof": res[8], "material": res[9], "color": res[10], "img": res[3],
                    "stock": res[4], "cost": res[6], "price": res[5], "size": res[7], "quantity": res[12]})
    cur.close()
    conn.close()

    return productlist

def getamountModel():
    amount = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT sticker_id, quantity FROM cont NATURAL JOIN orders WHERE order_id = (SELECT MAX(order_id) from orders WHERE customer_id = %s)", session['customer'])
    results = cur.fetchall()
    for res in results:
        amount.append({"sticker_id": res[0], "quantity": res[1]})
    cur.close()
    conn.close()

    return amount

def getdateModel():
    date = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT day FROM cont WHERE order_id = (SELECT MAX(order_id) FROM orders WHERE customer_id = %s)", session['customer'])
    results = cur.fetchall()
    for res in results:
        date.append({"date": res[0]})
    cur.close()
    conn.close()

    return date
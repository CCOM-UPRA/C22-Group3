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
    cur.execute("SELECT DISTINCT orders.tracking_number, orders.price_total, cont.day, orders.order_id FROM orders JOIN cont ON orders.order_id = cont.order_id WHERE orders.customer_id = %s;",(session['customer']))
    results = cur.fetchall()
    print(results)
    
    for res in results:
        products = []
        amountproducts = 0
        cur.execute("SELECT s_name, image_link, s_brand, cont.price, cont.quantity FROM cont JOIN stickers ON cont.sticker_id = stickers.sticker_id WHERE cont.order_id = %s;",(res[3]))
        results2 = cur.fetchall()
        for res2 in results2:
            products.append({"s_name": res2[0], "img": res2[1], "brand": res2[2], "price": res2[3], "quantity": res2[4]})
            amountproducts += res2[4]
        
        orderlist.append({"tracking": res[0], "total": res[1], "date": res[2], "o_id": res[3], "products": products, "amount": amountproducts})
    
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
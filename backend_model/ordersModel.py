from backend_model.profileModel import MagerDicts
from backend_model.connectDB import *

# ORDER 1
# ------------------------------------------------------------
#
orderDict1 = {"1": {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'delivered'
}}

# ORDER 2
# ------------------------------------------------------------
#
orderDict2 = {'2': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'shipped'

}}

# ORDER 3
# ------------------------------------------------------------
#
orderDict3 = {'3': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'processed'
}}

# ORDER 4
# ------------------------------------------------------------
#
orderDict4 = {'4': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'cancelled'
}}



# PRODUCTS
# ------------------------------------------------------------
productDict1 = {"1": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '1'
}}

productDict2 = {"2": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '1'
}}

productDict3 = {"3": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '3'
}}

productDict4 = {"4": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '2'
}}

productDict5 = {"5": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '4'
}}

productDict6 = {"6": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '2'
}}


ordersList = MagerDicts(orderDict1, orderDict2)
ordersList = MagerDicts(ordersList, orderDict3)
ordersList = MagerDicts(ordersList, orderDict4)

productsList = MagerDicts(productDict1, productDict2)
productsList = MagerDicts(productsList, productDict3)
productsList = MagerDicts(productsList, productDict4)
productsList = MagerDicts(productsList, productDict5)
productsList = MagerDicts(productsList, productDict6)


def ordersModel():
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    orderlist = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT order_id, customer_id, tracking_number, o_status, day, price_total FROM orders NATURAL JOIN cont ;")
    results = cur.fetchall()
    
    for res in results:
        orderlist.append({"o_id": res[0], "c_id": res[1], "tracking": res[2], "o_status": res[3], "date": res[4], "total": res[5]})
    
    cur.close()
    conn.close()

    return orderlist


def filterOrdersModel(search, column):
    # DB credentials found in backend_model/connectDB.py
    #db = Dbconnect()
    #orders = []
    #if column == "customer":
    #    query = "SELECT * FROM orders WHERE customer_id = %s"
    #elif column == "order":
    #    query = "SELECT * FROM orders WHERE order_id = %s"

    #ordersFound = db.select(query, search)
    #for o in ordersFound:
    #    orders.append({"id": o['order_id'], "c_id": o['c_id'], "tracking": o['tracking_number'], "transaction":
    #                   o['transaction_number'], "order_date": o['order_date'], "arrival_date": o['arrival_date'],
    #                   "ship_date": o['ship_date'], "total_price": o['total_price'], "status": o['order_status']})
    #return orders
    db = Dbconnect()
    orderlist = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    if column == "customer":
        cur.execute("SELECT DISTINCT order_id, customer_id, tracking_number, o_status, day, price_total FROM orders NATURAL JOIN cont WHERE customer_id = %s;",(search))
    else:
        cur.execute("SELECT DISTINCT order_id, customer_id, tracking_number, o_status, day, price_total FROM orders NATURAL JOIN cont WHERE order_id = %s;",(search))
    results = cur.fetchall()
    
    for res in results:
        orderlist.append({"o_id": res[0], "c_id": res[1], "tracking": res[2], "o_status": res[3], "date": res[4], "total": res[5]})
    
    cur.close()
    conn.close()

    return orderlist


def getordermodel(ID):
    #for key, order in ordersList.items():
    #    if key == ID:
    #        return order
    db = Dbconnect()
    orderlist = []
    quantity = 0
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT quantity, sticker_id FROM orders NATURAL JOIN cont WHERE order_id = %s;",(ID))
    quan = cur.fetchall()
    for sticker in quan:
        quantity = quantity + sticker[0]
    cur.execute("SELECT DISTINCT o_status, day, price_total FROM orders NATURAL JOIN cont WHERE order_id = %s;",(ID))
    results = cur.fetchall()
    
    for res in results:
        orderlist.append({"o_status": res[0], "date": res[1], "total": res[2], "quantity": quantity})
    
    cur.close()
    conn.close()

    return orderlist


def getorderproductsmodel(ID):
    returnList = {}
    total = 0
    #num = 1
    #for key, product in productsList.items():
    #    if product['order_id'] == ID:
    #        if returnList == {}:
    #            returnList = {'1': product}
    #        else:
    #            num += 1
    #            returnList = MagerDicts(returnList, {str(num): product})
    #print(returnList)
    db = Dbconnect()
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT  sticker_id, s_name, s_brand, price, quantity FROM stickers NATURAL JOIN cont WHERE order_id = %s;", (ID))
    results = cur.fetchall()

    for res in results:
        total = res[3] * res[4]
        product = {
            "s_id": res[0],
            "name": res[1],
            "brand": res[2],
            "price": res[3],
            "quantity": res[4],
            "total": total
        }
        if not returnList:
            returnList['1'] = product
        else:
            num = len(returnList) + 1
            returnList[str(num)] = product
        total = 0

    cur.close()
    conn.close()

    return returnList

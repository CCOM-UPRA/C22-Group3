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
    cur.execute("SELECT DISTINCT tracking_number, price_total, day, order_id FROM orders NATURAL JOIN cont ;")
    results = cur.fetchall()
    
    for res in results:
        products = []
        amountproducts = 0
        cur.execute("SELECT s_name, image_link, s_brand, price, quantity FROM orders NATURAL JOIN cont NATURAL JOIN stickers GROUP BY s_name")
        results2 = cur.fetchall()
        
        for res2 in results2:
            products.append({"s_name": res2[0], "img": res2[1], "brand": res2[2], "price": res2[3], "quantity": res2[4],})
            amountproducts = amountproducts + res2[4]
        orderlist.append({"tracking": res[0], "total": res[1], "date": res[2], "o_id": res[3], "products": products, "amount": amountproducts})
    
    cur.close()
    conn.close()

    return orderlist


def filterOrdersModel(search, column):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    orders = []
    if column == "customer":
        query = "SELECT * FROM orders WHERE c_id = %s"
    elif column == "order":
        query = "SELECT * FROM orders WHERE order_id = %s"

    ordersFound = db.select(query, search)
    for o in ordersFound:
        orders.append({"id": o['order_id'], "c_id": o['c_id'], "tracking": o['tracking_number'], "transaction":
                       o['transaction_number'], "order_date": o['order_date'], "arrival_date": o['arrival_date'],
                       "ship_date": o['ship_date'], "total_price": o['total_price'], "status": o['order_status']})
    return orders


def getordermodel(ID):
    for key, order in ordersList.items():
        if key == ID:
            return order


def getorderproductsmodel(ID):
    returnList = {}
    num = 1
    for key, product in productsList.items():
        if product['order_id'] == ID:
            if returnList == {}:
                returnList = {'1': product}
            else:
                num += 1
                returnList = MagerDicts(returnList, {str(num): product})
    print(returnList)
    return returnList





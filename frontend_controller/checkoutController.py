from flask import url_for, redirect
from frontend_model.checkoutModel import *
import pymysql
import datetime
import random

def validateUserCheckout():
    # Find the user in DB via checkoutModel function
    user = validateUserModel()

    for u in user:

        # Check if a specific part is empty/null/0/etc and save the appropriate message to send back to checkout
        # Checkout will display an error message according to the variable 'message' if some info is missing
        # Otherwise, it will proceed to invoice
        if u['p_brand'] == "" or u['cardyear'] == "" or u['cardmon'] == "" or u['card_number'] == "":
            message = "payment"
            return redirect(url_for('checkout', message=message))
        elif u['phone_number'] == 0:
            message = "number"
            return redirect(url_for('checkout', message=message))
        elif u['city'] == "" or u['state'] == "" or u['zipcode'] == "" or u['street'] == "":
            message = "address"
            return redirect(url_for('checkout', message=message))
        else:
            
            #add the checkout info into the database, 
            conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918', user='sql9607918', password='GFQC75Bg2g', port=3306)
            cur = conn.cursor()
            
            #create a random trakcing number
            traking_num = ''.join([str(random.randint(0, 9)) for _ in range(18)])
            orderinfo = [traking_num, session['total'], u['id']]
            inf = tuple(orderinfo)
            #First we create the order. 
            cur.execute("INSERT INTO orders (tracking_number, price_total, o_status, customer_id) VALUES (%s, %s, 'placed', %s)", inf)
            conn.commit()
            #next we need the id of the latest order we just added to the database
            cur.execute("SELECT MAX(order_id) FROM orders")
            orderID = cur.fetchall()
            #now we iterate through every itme in the shopping cart and add it to our contains table
            for key, item in session['cart'].items():
                dt = datetime.datetime.now()
                date = dt.strftime("%Y-%m-%d")
                
                iteminfo = [key, orderID, item['quantity'], item['price'], date]
                iteminf = tuple(iteminfo)
                cur.execute("INSERT INTO cont (sticker_id, order_id, quantity, price, day) VALUES (%s, %s, %s, %s, %s)", iteminf)
                conn.commit()
                #Update the table of products to reduce the stock by the amount purchased
                info2 = [item['quantity'], key]
                inf2 = tuple(info2)
                cur.execute("UPDATE stickers SET stock = stock - %s WHERE sticker_id = %s", inf2)
                conn.commit()
                

            session['cart'] = {}
            cur.close()
            conn.close()
            return redirect("/invoice")


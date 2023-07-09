from backend_model.connectDB import *


def getProductsModel():
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    productList = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM stickers")
    results = cur.fetchall()
    for res in results:
        productList.append({"id": res[0], "name": res[1], "brand": res[11], "desc": res[2],
                    "waterproof": res[8], "material": res[9], "color": res[10], "img": res[3],
                    "stock": res[4], "cost": res[6], "price": res[5], "size": res[7], "status": res[12]})
    cur.close()
    conn.close()
    return productList


# Find the specific product given the ID
def getsingleproductmodel(prodID):
    # TO BE ADDED BY STUDENTS
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM stickers WHERE sticker_id = %s LIMIT 1", (prodID,))
    result = cur.fetchone()
    if result:
        product = {
            "id": result[0],
            "name": result[1],
            "brand": result[11],
            "desc": result[2],
            "waterproof": result[8],
            "material": result[9],
            "color": result[10],
            "img": result[3],
            "stock": result[4],
            "cost": result[6],
            "price": result[5],
            "size": result[7],
            "status": result[12]
        }
    else:
        product = None
    cur.close()
    conn.close()
    return product


def createNewProductmodel(name, brand, desc, material, size, water, color, cost, price, img, stock, status):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    query = "INSERT INTO stickers(sticker_id, s_name, s_brand, description, material, size, waterproof, color, cost, price," \
            "image_link, stock, s_status) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    db.execute(query, (name, brand, desc, material, size, water, color, cost, price, img, stock, status))
    return

def updateproductmodel(name, brand, desc, material, size, water, color, cost, price, img , stock, status, id):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE stickers SET s_name = %s, s_brand = %s, description = %s, material = %s, size = %s, waterproof = %s,"
                    "color = %s, cost = %s, price = %s, image_link = %s, stock = %s, s_status = %s WHERE sticker_id = %s",
                    (name, brand, desc, material, size, water, color, cost, price, img, stock, status, id))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1
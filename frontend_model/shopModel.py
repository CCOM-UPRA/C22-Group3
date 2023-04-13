import pymysql

# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences
#               Old order of ProductList.append
# "id": res[0], "name": res[1], "brand": res[2], "desc": res[3]
# "wifi": res[4], "video_res": res[5], "color": res[6], "img": res[7],
# "stock": res[8], "cost": res[9], "price": res[10], "status": res[11]

productList = [['1', "Tello Drone", 'DJI', 'desc here', 'Yes', '480p', 'White', 'dji_tello.jpg', '15', 'active', '89', '89'],
               ['2', 'Bebop 2', 'Parrot', 'desc', 'Yes', '1080p', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270', '290']]


def getProductsModel():
    productList = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * from stickers")
    results = cur.fetchall()
    for res in results:
        productList.append({"id": res[0], "name": res[1], "brand": res[11], "desc": res[2],
                    "waterproof": res[8], "material": res[9], "color": res[10], "img": res[3],
                    "stock": res[4], "cost": res[6], "price": res[5], "size": res[7]})
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["DJI", "Ruko", "Parrot"]
    return brands

def getColorsModel():
    colors = ["White", "Gray", "Red"]
    return colors


def getVideoResModel():
   videores = ["480p", "1080p", "4k"]
   return videores


def getWifiModel():
    wifi = ['Yes', 'No']
    return wifi

# new code for buttons

def getMaterialModel():

    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    c = conn.cursor()
    c.execute('SELECT DISTINCT material FROM stickers')
    material = [row[0] for row in c.fetchall()]
    c.close()
    conn.close()
    return material

def getSizeModel():

    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    c = conn.cursor()
    c.execute('SELECT DISTINCT size FROM stickers')
    size = [row[0] for row in c.fetchall()]
    c.close()
    conn.close()
    return size

def getColorModel():

    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    c = conn.cursor()
    c.execute('SELECT DISTINCT color FROM stickers')
    colors = [row[0] for row in c.fetchall()]
    c.close()
    conn.close()
    return colors

def getWaterProofModel():

    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9607918',
                           user='sql9607918', password='GFQC75Bg2g', port=3306)
    c = conn.cursor()
    c.execute('SELECT DISTINCT waterproof FROM stickers')
    waterproof = [row[0] for row in c.fetchall()]
    c.close()
    conn.close()
    return waterproof
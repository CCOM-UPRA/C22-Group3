from backend_model.productsModel import *


def getProducts():
    products = getProductsModel()
    return products


def getsingleproduct(prodID):
    # TO BE ADDED BY STUDENTS
    return getsingleproductmodel(prodID)


def createNewProduct(name, brand, video_res, wifi, color, price, cost, stock, img, status):
    price = float(price)
    cost = float(cost)
    stock = int(stock)

def updateproductcontroller(name, brand, desc, material, size, water, color, cost, price, img , stock, status):
    return updateproductmodel(name, brand, desc, material, size, water, color, cost, price, img , stock, status)

    return createNewProductModel(name, brand, video_res, wifi, color, price, cost, stock, img, status)

from backend_model.productsModel import *


def getProducts():
    products = getProductsModel()
    return products


def getsingleproduct(prodID):
    # TO BE ADDED BY STUDENTS
    return getsingleproductmodel(prodID)


def createNewProduct(name, brand, desc, material, size, water, color, cost, price, img , stock, status):
    price = float(price)
    cost = float(cost)
    stock = int(stock)
    createNewProductmodel(name, brand, desc, material, size, water, color, cost, price, img , stock, status)

def updateproductcontroller(name, brand, desc, material, size, water, color, cost, price, img , stock, status, id):
    return updateproductmodel(name, brand, desc, material, size, water, color, cost, price, img , stock, status, id)
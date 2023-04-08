from frontend_model.shopModel import *
#=========================================================================================================================================================================================================================================
#new controller

def getNewProducts():
    newproducts = getNewProductsModel()
    return newproducts

def getNewProductAscending():
    newproducts = sort_newproductlistAscending(getNewProductsModel())
    return newproducts

def getNewProductDescending():
    newproducts = sort_newproductlistDescending(getNewProductsModel())
    return newproducts

def getSize():
    return getSizeModel()

def getWaterProof():
    return getWaterProofModel()

def getMaterial():
    return getMaterialModel()

def getPrimaryColor():
    return getPrimaryColorModel()

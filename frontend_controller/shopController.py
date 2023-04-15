from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products

def getFilteredProducts(size, waterproof, material, color):
    products = getFilterModel(size, waterproof, material, color)
    return products

def getSize():
    return getSizeModel()

def getWaterProof():
    return getWaterProofModel()

def getMaterial():
    return getMaterialModel()

def getColor():
    return getColorModel()

def getBrands():
    return getBrandsModel()

def getVideoRes():
    return getVideoResModel()
#old
def getColors():
    return getColorsModel()

def getWifi():
    return getWifiModel()
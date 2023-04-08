# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences    
#====================================New Code testing===================================================================================================================================================================================                        
                        #New order
                              # Make sure ImageLink is ID+Name.png (DeleteSpaces,lowercase)
# ID 0, Name 1, ImageLink 2, Stock 3, 
# Size 4
# WaterProof 5, Price 6, Cost 7,
# Material 8, 
# Color 9, Brand 10, Description 11

newproductList = [['1','Bad Bunny Icon','1badbunnyicon.png','13','Custom','Yes','15','6.5','Solid','Red','Bad Bunny','The iconic heart from Bad Bunnys album art.'],
                  ['2','Bugatti Logo','2bugattilogo.png','7','Oval','Yes','9','5','Solid','Red','Bad Bunny','The iconic heart from Bad Bunnys album art.']]

#=========================================================================================================================================================================================================================================
                                #new Model     
def getNewProductsModel():
    return newproductList

def sort_newproductlistAscending(awa):
    awa = sorted(newproductList, key=lambda product: int(product[6]))
    return awa

def sort_newproductlistDescending(ewe):
   ewe = sorted(newproductList, key=lambda product: int(product[6]),reverse = True)        
   return ewe

def getSizeModel():
    size = ["Square 5x5", "Square 3x3","Circle","Bumper","Oval","Custom"]
    return size

def getWaterProofModel():
    waterproof = ['Yes', 'No']
    return waterproof

def getMaterialModel():
    material = ["Solid","Glossy","Metallic"]
    return material

def getPrimaryColorModel():
    primarycolor = ["Rainbow","Monocrome","Red","Blue","Yellow","Orange","Green","Purple","Pink","Brown"]
    return primarycolor

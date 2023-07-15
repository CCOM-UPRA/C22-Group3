from backend_model.accountsModel import *


def getaccounts(userType):
    return getaccountsmodel(userType)


def getaccount(acc, userType):
    return getaccountmodel(acc, userType)


def updateAccountController(userInfo, userType, id, kind):
    return updateAccountModel(userInfo, userType, id, kind)

def getpaymentaccount(acc):
    return getpaymentaccountmodel(acc)

def createaccountcontroller(userInfo):
    return createaccountmodel(userInfo)
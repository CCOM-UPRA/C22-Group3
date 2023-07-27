from backend_model.profileModel import *

def getUser():
    return getUserModel()

def updateprofilecontroller(fname, lname, email, status, aid):
    return updateprofilemodel(fname, lname, email, status, aid)

def updatepasswordcontroller(oldpass, pass1, adminid):
    return updatepasswordmodel(oldpass, pass1, adminid)
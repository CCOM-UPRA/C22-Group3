from frontend_model.registerModel import *
from flask import redirect, render_template

def registercontroller(registerinfo):
    #TODO replicate the process in the login but to just add stuff to the database
    #we validate the data inside the model, if we ever need to check for stuff do it here
    result = registermodel(registerinfo = registerinfo)
from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False



def getCartModel():
    # Initialize the amount and totaL for the cart
    session['amount'] = 0
    session['total'] = 0
    if 'cart' in session:
        for key, item in session['cart'].items():
            session['amount'] += int(item['quantity'])
            session['total'] += float(item['total_price'])
        return session['cart']
    else:
        return


def addCartModel(dictitems):
    # Add new product to cart using MagerDicts if cart already has items in
    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems)
    else:
        session['cart'] = dictitems

    # Update the session variables with the new additions
    # Pointer: POST variables can sometimes end up returning strings, so we must type_cast our variables for the operations
    session['amount'] = 0
    session['total'] = 0
    for key, item in session['cart'].items():
        session['amount'] += int(item['quantity'])
        session['total'] += float(item['total_price'])
    return


def deleteCartItemModel(id):
    # get the cart dictionary from the session
    cart = session.get('cart', {})
    print(cart)
    str_id = str(id)
    del cart[str_id]
    print(cart)
    session['cart'] = cart
    #del session['cart'][id]
    # FOR STUDENT TO ADD
    return

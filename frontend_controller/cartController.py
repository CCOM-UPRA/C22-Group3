from frontend_model.cartModel import *


def getCart():
    # Go to cartModel to get cart items and session variables: total and quantity
    return getCartModel()


def addCartController(p_id, name, image, price, quantity, stock, total):
    # Receive the variables that we got from POST originally and save in a dictItem to add to session cart
    # The add happens over at the cartModel
    dictitems = {p_id: {'name': name, 'image': image, 'price': price, 'quantity': quantity, 'stock': stock,
                        'total_price': total}}
    return addCartModel(dictitems)


def deleteCartItem(id):
    # FOR STUDENT TO ADD
    return deleteCartItemModel(id)

def getCartItem(p_id):
    if 'cart' in session:
        cart = session['cart']
        if p_id in cart:
            return cart[p_id]
    return None

def updateCartItem(p_id, new_quantity, new_total):
    if 'cart' in session:
        cart = session['cart']
        if p_id in cart:
            cart_item = cart[p_id]
            old_quantity = int(cart_item['quantity'])
            old_total = float(cart_item['total_price'])
            quantity_diff = int(new_quantity) - old_quantity
            total_diff = float(new_total) - old_total
            
            
            if new_quantity <= int(cart_item['stock']):
                cart_item['quantity'] = new_quantity
                cart_item['total_price'] = new_total
                session['cart'] = cart
                session['amount'] += quantity_diff
                session['total'] += total_diff
                return True
    return False
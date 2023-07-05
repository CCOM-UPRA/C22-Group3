from flask import Flask, render_template, redirect, request, session
from frontend_controller.cartController import *
from frontend_controller.checkoutController import *
from frontend_controller.invoiceController import *
from frontend_controller.loginController import *
from frontend_controller.ordersController import *
from frontend_controller.profileController import *
from frontend_controller.shopController import *
from frontend_controller.registerController import *
from passlib.hash import sha256_crypt


app = Flask(__name__, template_folder='frontend/')
app.secret_key = 'akeythatissecret'

# In this template, you will usually find functions with comments tying them to a specific controller
# main.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app
# LOGIN INFO:
    # javier.quinones3@upr.edu (pass1234)


# Redirects us here if no url is given
@app.route("/", defaults={'message': None})
# Or if any url other than the ones set in this Flask application is provided, making it a <message>
@app.route("/<message>")
def enterpage(message):

    if message is None:
        return redirect("/shop")
    elif message == 'enter':
        return render_template('login (2).html')
    else:
        return render_template('login (2).html', message=message)


@app.route("/change")
def change():
    # An optional function for students to hash a specific password
    # changePass function can be found in profileController
    # Access this function by typing the word 'change' after your Flask url
    # http://127.0.0.1:5000/change
    changePass()
    return render_template("login (2).html")


@app.route("/clear")
def clear():
    # Whenever you wish to log out or clear the session info, you can type /clear at the end of the Flask address
    session.clear()
    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
    # Enters here when logging in
    email = request.form.get('email')
    passcode = request.form.get('password')
    # Receive your login information and send to the loginController's logincontroller()

    return logincontroller(email=email, password=passcode)


@app.route("/register/", defaults={'message': None})
@app.route('/register/<message>')
def register(message):
    # TO BE CONNECTED TO MYSQL BY STUDENTS
    # Redirects to register page

    # First must verify if user is already in DB, if not, then proceed with register

    # Example of an INSERT query:
    # INSERT
    # INTO
    # Customers(CustomerName, ContactName, Address, City, PostalCode, Country)
    # VALUES('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

    # Also worth pointing out, password must be hashed before adding to DB:
    # sha256_crypt.encrypt(unhashed_password_here)
    # This is the example of hashing I utilize, but there are many forms of using hashing/encryption of passwords
    return render_template('register.html', message=message)
    

@app.route("/registerinfo", methods=['POST'])
def registerinfo():
    # TO BE CONNECTED TO MYSQL BY STUDENTS
    # Process the register info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')
    phone = request.form.get('phone')
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')

    if email_already_in_use(email):
        return redirect('/register/Email already in use')

    if not fname or not lname or not email or not phone or not street or not city or not state or not zipcode:
        return redirect('/register/Please fill in all fields')
    
    if not phone.isdigit():
        return redirect('/register/Phone number should contain only digits')
    
    if len(phone) != 10:
        return redirect('/register/Phone number should be 10 digits')
    
    if not state.isalpha():
        return redirect('/register/State should contain only letters')

    if len(state) != 2:
        return redirect('/register/State should be 2 characters')

    if len(zipcode) != 5:
        return redirect('/register/Zip code should be 5 digits')

    if '@' not in email:
        return redirect('/register/Invalid email format')

    if pass1 == pass2:
        if len(pass1) >= 8 and len(pass1) <= 16:
            # Process register info here
            # For now, we won't have the register log you in when you create an account but rather take you to the log in screen afterwards
            passcode = sha256_crypt.encrypt(pass1)
            pass1 = passcode
            registerinfo = [fname, lname, email, pass1, phone, street, city, state, zipcode]
            registercontroller(registerinfo=registerinfo)
            return redirect('/login')
        else:
            return redirect('/register/Invalid password length')
    else:
        return redirect('/register/Passwords do not match')


@app.route("/shop", methods=["GET", "POST"])
def shop():
    if request.method == "POST" and request.form:
        size = request.form.get("Si")
        waterproof = request.form.get("Wat")
        material = request.form.get("Mat")
        color = request.form.get("Co")
        order = request.form.get("Order")
        name = request.form.get("StickerName")
        products = getFilteredProducts(size, waterproof, material, color, order, name)
    else:
        products = getProducts()

    
    getCart()
    sizeo = getSize()
    waterproofo = getWaterProof()
    materialo = getMaterial()
    colorso = getColor()

    return render_template("shop-4column.html", products=products, size=sizeo, waterproof=waterproofo,
                           material=materialo, colors=colorso)
@app.route("/profile")
def profile():
    # To open the user's profile page
    # Get user info from getUser() in profileController
    user = getUser()
    payments = getPayment()

    # Since I specified the variable as user1, that is how it will be called on the html page
    return render_template("profile.html", user=user, payments=payments)


@app.route("/editinfo", methods=["POST"])
def editinfo():
    # If editing phone_number, edit phone_number -> profileController
    if 'number' in request.form:
        number = request.form.get('number')
        editnumbercontroller(number)

    # If editing address info, edit address -> profileController
    elif 'street' in request.form:
        street = request.form.get('street')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        city = request.form.get('city')
        editaddresscontroller(street, state, zipcode, city)

    # If editing payment info -> profileController
    elif 'card_num' in request.form:
        old_num = request.form.get('old_card_num')
        c_type = request.form.get('card_type')
        number = request.form.get('card_num')
        exp_mon = request.form.get('card_month')
        exp_year = request.form.get('card_year')
        p_zipcode = request.form.get('p_zipcode')
        editpaymentcontroller(old_num, c_type, number, exp_mon, exp_year, p_zipcode)

    # If editing main info -> profileController
    elif 'fname' in request.form:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        editprofilecontroller(fname, lname, email)

    # Checks if you're editing from your profile page or your checkout page
    if 'profile' in request.form:
        return redirect("/profile")
    elif 'checkout' in request.form:
        return redirect("/checkout")
    
@app.route("/add_card", methods=["POST"])
def add_card():

    c_type = request.form.get('card_type')
    number = request.form.get('card_num')
    exp_mon = request.form.get('card_month')
    exp_year = request.form.get('card_year')
    p_zipcode = request.form.get('p_zipcode')
    addcardcontroller(c_type, number, exp_mon, exp_year, p_zipcode)
    
    if 'profile' in request.form:
        return redirect("/profile")
    elif 'checkout' in request.form:
        return redirect("/checkout")
    
@app.route("/del_card", methods=["POST"])
def del_card():
    del_num = request.form.get('del_num')
    delcardcontroller(del_num)
    return redirect("/profile")


@app.route("/password", methods=["GET", "POST"])
def password():

    if request.method == "POST" and request.form:
        npass = request.form.get("pass_n1")
        email = request.form.get("email")
        changePass(npass, email)


    # TO BE CONNECTED TO MYSQL BY STUDENTS
    return render_template("change-password.html")



@app.route("/orders")
def orders():
    # Redirects us to the orders list page of the user
    # Fetches each order and its products from ordersController
    orders = getOrdero()
    user = getUser()
    amount = 0
    for order in orders:
        amount = amount + 1
    return render_template("orderlist.html", orders=orders, user=user, amount = amount)


@app.route("/addcart", methods=["POST"])
def addcart():
    # Get the relevant info for product to add to cart
    p_id = request.form.get('p_id')
    name = request.form.get('name')
    image = request.form.get('image')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    stock = request.form.get('stock')
    total = float(price) * int(quantity)

    cart_item = getCartItem(p_id)  # Implement this function to get cart item by product ID
    if cart_item:
        # Item already exists in the cart, update the quantity and total
        new_quantity = int(cart_item['quantity']) + int(quantity)
        for key, value in cart_item.items():
           print(key, value)
        new_total = float(cart_item['total_price']) + total
        updateCartItem(p_id, new_quantity, round(new_total, 2))  # Implement this function to update the cart item
    else:
        # Item doesn't exist in the cart, add it
        addCartController(p_id, name, image, price, quantity, stock, round(total, 2))

    # Redirect back to the previous page
    return redirect(request.referrer)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # TO BE ADDED BY STUDENTS (Editing the session variable cart)
    deleteCartItem(id)
    return redirect(request.referrer)


@app.route("/editcart", methods=["POST"])
def editcart():
    # TO BE ADDED BY STUDENTS (Editing the session variable cart)
    p_id = request.form.get('pid')
    name = request.form.get('name')
    image = request.form.get('image')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    stock = request.form.get('stock')
    total = float(price) * int(quantity)

    deleteCartItem(p_id)
    addCartController(p_id, name, image, price, quantity, stock, total)

    return redirect(request.referrer)


@app.route("/checkout/", defaults={'message': None})
@app.route("/checkout/<message>")
def checkout(message):
    # Check if customer is logged in
    if 'customer' in session:
        # > profileController
        user = getUser()
        payments = getPayment()

        return render_template("checkout.html", user=user, message=message, payments=payments)

    else:
        # If customer isn't logged in, create session variable to tell us we're headed to checkout
        # Redirect us to login with message
        session['checkout'] = True
        return redirect("/wrong")


@app.route("/validate")
def validate():
    # Validates whether all user info is complete before processing the checkout
    # -> checkoutController
    return validateUserCheckout()


@app.route("/invoice")
def invoice():
    # TO BE CONNECTED TO MYSQL BY STUDENTS
    # > invoiceController
    order = getOrder()
    products = getOrderProducts()
    amount = getamount()
    totalitem = 0
    for item in amount:
        totalitem += item['quantity']
    user = getUser()
    date = getdate()
    payment = getPayment()
    return render_template("invoice.html", order=order, products=products, amount=amount, totalitem=totalitem, user=user, date=date, payment=payment)


#@app.route("/filter")
#def filter():
    # TO BE CONNECTED TO MYSQL BY STUDENTS




 #   return redirect("/shop")
#
@app.route("/filter", methods=['GET', 'POST'])
def filter():
        size = request.form['Size']
        if size == None:
            size = 1
        waterproof = request.form['Waterproof']
        if waterproof == None:
            waterproof = 1
        material = request.form['Mat']
        if material == None:
            material = 1
        color = request.form['testing']
        if color == None:
            color = 1
    #    return redirect("/shop?size={size}&waterproof={waterproof}&material={material}&color={color})
        return redirect("/shop/" + (size or "") + "/" + (waterproof or "") + "/" + (material or "") + "/" + (color or ""))

  #  return redirect("/shop")
#
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
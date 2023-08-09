import os
from datetime import datetime, timedelta
from time import strftime

from flask import Flask, render_template, redirect, request, session, url_for
from werkzeug.utils import secure_filename

from backend_controller.loginController import *
from backend_controller.ordersController import *
from backend_controller.productsController import *
from backend_controller.accountsController import *
from backend_controller.reportsController import getDatedReport, getStockReport, getReport, getNames, getimagecontroller
from backend_controller.profileController import *
from backend_controller.changePassController import *

# In this template, you will usually find functions with comments tying them to a specific controller
# admin.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app
# You will find functions that access dummy data, this is for students to see a template of what to expect
# However, final project should have 100% Database connection

app = Flask(__name__, template_folder='backend/')
app.secret_key = 'akeythatissecret'


@app.route("/", defaults={'message': None})
@app.route("/<message>")
def enterpage(message):
    return render_template('login (2).html', message=message)


@app.route("/clear")
def clear():
    # Clear session information
    session.clear()
    return redirect("/")


@app.route("/hashpass")
def hashpass():
    # For hashing already established unhashed passwords
    # changePassController ->
    changePass()
    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    session['amount'] = 0
    # POINTER: loginModel creates a session['admin'] instead
    # Always advisable to name your frontend and backend sessions differently to not cause errors via lingering sessions
    return logincontroller(email=email, password=password)


@app.route("/profile") 
def profile():
    # VIEW AND EDIT PERSONAL PROFILE LEFT FOR STUDENTS TO ADD
    # -> profileController.py
    admin = getUser()
    return render_template("profile.html", user1=admin)


@app.route("/editinfo", methods=["POST"])
def editinfo():
    # make changes to profile info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    status = request.form.get('status')
    aid = request.form.get('ID')

    updateprofilecontroller(fname, lname, email, status, aid)
    return redirect("/profile")


@app.route("/password")
def password():
    adminid = request.args.get('adminid')
    # make password changes
    # optional for students to implement or not
    return render_template("change-password.html", adminid=adminid)

@app.route("/updatepassword", methods=["POST"])
def updatepassword():
    oldpass = request.form.get('oldpass')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')
    adminid = request.form.get('adminid')
    if pass1 == "" or pass2 == "":
         return render_template("change-password.html", adminid=adminid, message = "incomplete")
    if pass1 != pass2:
        return render_template("change-password.html", adminid=adminid, message = "nomatch")
    else:
        suc = updatepasswordcontroller(oldpass, pass1, adminid)
        if suc:
            return render_template("change-password.html", adminid=adminid, message = "changed")
        else:
            return render_template("change-password.html", adminid=adminid, message = "wrong")

@app.route("/products")
def products():
    productsp = getProducts()
    return render_template("products.html", products=productsp)


@app.route("/single_product/<prodID>")
def single_product(prodID):
    # Return product page for single product selected
    # TO BE ADDED BY STUDENTS (missing DB connection, shows dummy data in HTML)
    product = getsingleproduct(prodID)
    return render_template("single_product.html", product=product)


@app.route("/editproduct", methods=['POST'])
def editproduct():
    id = request.form.get('id')
    name = request.form.get('name')
    brand = request.form.get('brand')
    desc = request.form.get('desc')
    material = request.form.get('material')
    size = request.form.get('size')
    water = request.form.get('waterproof')
    color = request.form.get('color')
    cost = request.form.get('cost')
    price = request.form.get('price')
    img = request.form.get('img')
    stock = request.form.get('stock')
    status = request.form.get('status')
    updateproductcontroller(name, brand, desc, material, size, water, color, cost, price, img , stock, status, id)
    return redirect('/products')


@app.route("/addproduct/", defaults={'message': None})
@app.route("/addproduct/<message>")
def addproduct(message):
    # Enter the add product page, will show a message sent from createproduct() once a product is created.
    return render_template("add_product.html", message=message)


@app.route("/createproduct", methods=['POST'])
def createproduct():
    # Receive data from add_product.html
    name = request.form.get('name')
    brand = request.form.get('brand')
    desc = request.form.get('desc')
    material = request.form.get('material')
    size = request.form.get('size')
    water = request.form.get('waterproof')
    color = request.form.get('color')
    cost = request.form.get('cost')
    price = request.form.get('price')
    img_link = request.form.get('img_link')
    stock = request.form.get('stock')
    status = request.form.get('status')

    # Photo is received from a file and will save the file into your product-images folder
    img = request.files['imgfile']
    img2 = img
    filename = secure_filename(img.filename)
    # Adjust to your directory
    # WARNING: Can cause issues if filename has spaces
    img.save(os.path.join(r"C:\Users\Emanuel\Documents\GitHub\C22-Group3\static\images\product-images", filename))

    print("img: ", img2.filename)

    # -> productsController.py
    createNewProduct(name, brand, desc, material, size, water, color, cost, price, img_link , stock, status)

    # Send message back to html page that product has been added
    message = 'added'
    return render_template("add_product.html", message=message)


@app.route("/accounts")
def accounts():
    # userType = accounts can be viewed by customers or admins
    # If a userType was specified, receive it
    if request.method == 'GET' and 'userType' in request.args:
        userType = request.args.get('userType')
    else:
        # Otherwise default to customer
        userType = 'customer'

    # Retrieve all accounts from 'database' and redirect us to accounts page
    # -> accountsController.py
    acc = getaccounts(userType)
    return render_template("accounts.html", accounts=acc, userType=userType)


@app.route("/createaccount")
def createaccount():
    # Redirect us to account creation page
    # TO BE ADDED BY STUDENTS
    return render_template("create_account.html")

@app.route("/addaccount", methods=['POST'])
def addaccount():
    name = request.form.get('fname')
    last = request.form.get('lname')
    number = request.form.get('pnumber')
    email = request.form.get('email')
    status = request.form.get('status')
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')
    password = request.form.get('pass')
    passworde = sha256_crypt.encrypt(password)
    userInfo = [name, last, number, email, status, street, city, state, zipcode, passworde]
    createaccountcontroller(userInfo)
    return render_template("create_account.html", message = "added")

@app.route("/editaccount/<acc>")
def editaccount(acc):
    # Fetch account given via url and then enter the edit page for that account
    # acc = customer or admin ID

    message = ""

    # Find userType, relevant for the query info
    if request.method == 'GET' and 'userType' in request.args:
        userType = request.args.get('userType')
    else:
        userType = 'customer'

    # Check if updateaccount() sent us a message of form completion to display
    if 'message' in request.args:
        message = request.args.get('message')

    # -> accountsController.py
    account = getaccount(acc, userType)
    #print("Account ID: ", acc)
    #print("UserType: ", userType)
    #print(account)
    if userType == 'customer':
        payments = getpaymentaccount(acc)
    else:
        payments = []
    return render_template("single_account.html", acc=account, userType=userType, message=message, payments=payments)


@app.route("/updateaccount", methods=['POST'])
def updateaccount():
    kind = request.form.get('change')
    id = request.form.get('id')
    userType = request.form.get('userType')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    status = request.form.get('status')

    if userType == 'customer' and kind == 'general':
        phone_number = request.form.get('pnumber')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        userInfo = [fname, lname, street, city, state, zipcode, phone_number, status]
        updateAccountController(userInfo, userType, id, kind)
    elif userType == 'customer' and kind == 'payment':
        number = request.form.get('cnumber')[-4:]
        brand = request.form.get('cbrand')
        expmon = request.form.get('expmon')
        expyear = request.form.get('expyear')
        czip = request.form.get('czip')
        pstatus = request.form.get('p_status')
        oldnum = request.form.get('oldnum')
        paymentinfo = (brand, expmon, expyear, czip, pstatus, number, oldnum)
        updateAccountController(paymentinfo, userType, id, kind)
    else:
        userInfo = [fname, lname, status]
        # Our user info will depend on whether we're updating an admin or customer
        # -> accountsController.py
        updateAccountController(userInfo, userType, id, "NULL")

    # Go back to edit page with message
    return redirect(url_for('editaccount', acc=id, userType=userType, message='added'))

@app.route("/deletepayment", methods=['POST'])
def deletepayment():
    c_id = request.form.get('id')
    p_num = request.form.get('num')
    deletepaymentcontroller(c_id, p_num)
    return redirect(url_for('accounts'))


@app.route("/orders")
def orders():
    # Fetches all the orders found in the 'database' to bring to orders page
    all_orders = ordersController()  # -> ordersController.py
    return render_template("orders.html", orders=all_orders)


@app.route("/orders_filter", methods=['POST'])
def orders_filter():

    # If search has been sent with info
    if "order_search" in request.form and request.form.get('order_search') != "":
        search = request.form.get('order_search')
        if search[0] == 'c':  # If string starts with c, look for orders by customer ID
            column = 'customer'
        elif search[0] == 'o':  # If string starts with o, look for orders by order ID
            column = 'order'
        else:
            return redirect("/orders")
        search = search[1:]  # Remove first char from string to search by numerical ID

        # -> ordersController.py
        all_orders = filterOrder(search, column)
        return render_template("orders.html", orders=all_orders)
    else:
        # Return full list of orders if search bar is empty
        return redirect("/orders")


@app.route('/editorder/<order>')
def editorder(order):
    # TO BE ADDED BY STUDENTS, HTML will only show dummy data
    # Receive from orders page an order via its id (our 'order' variable from the url)
    # Fetch the products in that order
    orderProducts = getorderproducts(order)
    # Fetch the order itself.
    order = getorder(order)
    # Go to separate page for that order
    return render_template('order.html', products=orderProducts, order=order)

@app.route("/updateorder/<order>", methods=['POST'])
def updateorder(order):
    ostatus = request.form.get('status')
    actualizarorden(order, ostatus)
    
    return redirect("/orders")


@app.route("/reports")
def reports():
    # Find all the distinct product names in DB
    # -> reportsController.py
    names = getNames()
    return render_template("reports.html", names=names)


@app.route("/product_report", methods=['POST'])
def product_report():
    # Function for Single Product Sales Report
    # All Products Sales and Inventory Reports are for STUDENTS TO ADD
    product = request.form.get('product')
    if "report_month" in request.form:
        print(request.form.get('report_month'))
        month = request.form.get('report_month')
        timeframe = "Month"
        start_date = month + "-01"   # Add start and end dates for query
        end_date = month + "-31"
        print(start_date)

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)

        # Date to show in title of page
        date = month

    elif "report_week" in request.form:
        timeframe = "Week"
        print("week: ", request.form.get('report_week'))
        week = request.form.get('report_week')
        start_date = datetime.strptime(week + '-1', "%Y-W%W-%w")
        end_date = start_date + timedelta(days=6)
        print(start_date, " - ", end_date)

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)
        start_date = start_date.strftime('%Y/%m/%d')
        end_date = end_date.strftime('%Y/%m/%d')

        # Date to show in title of page
        date = str(start_date) + " - " + str(end_date)

    elif "report_day" in request.form:
        timeframe = "Day"
        start_date = request.form.get('report_day')
        end_date = ""

        # -> reportsController.py
        orders = getReport(timeframe, start_date, end_date, product)

        # Date to show in title of page
        date = start_date

    # Calculate total ($ paid per order) and earnings = (price - cost) * quantity
    total = 0
    earnings = 0
    for order in orders:
        print(order)
        total += float(order['quantity'] * order['price'])
        total = round(total, 2)

        # Earnings part of order added in model
        earnings += float(order['earnings'])
        earnings = round(earnings, 2)

    # Timeframe: "Day", "Week", "Month"
    # product: product name for the HTML page to show
    # date: the range of dates used in the report for the HTML page to show
    if len(orders) > 0 and 'image_link' in orders[0]:
        pimage = orders[0]['image_link']
    else:
        pimage = getimagecontroller(product)

    return render_template("single_product_report.html", orders=orders,
                           timeframe=timeframe, date=date, total=total, earnings=earnings, product=product, pimage=pimage)


@app.route("/report", methods=['POST'])
def report():
    # THIS IS THE SAME REPORT WE HAD IN PHASE 1 WITH DUMMY
    # ALL PRODUCTS SALES AND INVENTORY REPORTS LEFT FOR STUDENTS TO ADD
    # Initialize variables to use
    date_report = {}
    stock_report = {}
    total = 0

    # If we're going for any of the reports that have a date, get the information and save in date_report
    # All cases give the same results in this case, no matter your date or product input
    if 'report_day' in request.form:
        day = request.form.get('report_day')
        frame = "day"
        end = ""
        date_report = getDatedReport(day, end, frame)
    if 'report_week' in request.form:
        week = request.form.get('report_week')
        start_date = datetime.strptime(week + '-1', "%Y-W%W-%w")
        end_date = start_date + timedelta(days=6)
        frame = "week"
        date_report = getDatedReport(start_date, end_date, frame)
    if 'report_month' in request.form:
        month = request.form.get('report_month')
        frame = "Month"
        start_date = month + "-01"
        end_date = month + "-31"
        date_report = getDatedReport(start_date, end_date, frame)

    # If we're going for the inventory/stock report, get the data and save in stock_report
    if 'stock_report' in request.form:
        stock_report = getStockReport()

    # If we're going for any of the reports with dates, we need a total at the end
    # Calculate the total according to the sum of the total_prices for each item in the report
    if date_report != {}:
        for order in date_report:
            total += float(order['quantity'] * order['price'])
            total = round(total, 2)
    
    earnings = 0
    for order in date_report:
        earnings += (order['price'] - order['cost']) * order['quantity']
        print(earnings)
    earnings = "{:.2f}".format(earnings)

    # We send to the report page all variables whether empty or not
    # The HTML will validate which variable is empty and will show the appropriate information
    return render_template("report.html", date_report=date_report, stock_report=stock_report, total=total, earnings=earnings)


# Press the green button in the gutter to run the script.
if __name__ == '__admin__':
    app.run(debug=True)

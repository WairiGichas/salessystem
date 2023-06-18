from flask import Flask, render_template
from pgfunc import fetch_data

# creating a variable to access the class this is an object (object)
# (_name_) the name is an object
# create an object called app
# name here(_name_) is used to tell Flask where to access HTML files
# all HTML files are put inside template folder
# all CSS/JS/Images are put inside "static" folder

app = Flask(__name__)

### CREATING ROUTES###

# a route is a an extension of a url which loads you to a html page
# /mat


# @app.route("/") #home route e.g techcamp.co.ke/ without "/" the route is null
# @ symbol is a decorator that means static route will not change
# a decorator expects a function declaration or def and ends with full colon.
# below the @ decorator BINDS the function home

# to return html file after the browser processes
@app.route("/")  # @ binds function home
def home():
    # To render a template, you use the render_template() method
    return render_template("index.html")


@app.route("/products")  # @ binds function about path
def products():
    prods= fetch_data ("products")
    # load records from our products table in the db
    # a list of tuples will be loaded

    return render_template('products.html', products = prods)

@app.route("/sales")  # @ binds function about path
def sales():
    sls= fetch_data ("sales")

    return render_template('sales.html', sales = sls)

@app.route("/dashboard")  # @ binds function about path
def dashboard():
     return render_template("dashboard")

@app.route("/stocks")  
# @ binds function about path
def stocks():
    return render_template("stocks")

@app.route("/inventories")  # @ binds function about path
def inventories():
     return render_template("inventories")


app.run()  # enables the app the run or to be executed

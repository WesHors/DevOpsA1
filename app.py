from flask import Flask, render_template

from pymongo import MongoClient

# Creates application instance
app = Flask(__name__)

# Creates mongodb client
mongodb_client = MongoClient("mongodb+srv://weshors:asdf1234@devopsdb.ddfwl.mongodb.net/?retryWrites=true&w=majority&appName=DevOpsDB")

db = mongodb_client["shop_db"]
products_collection = db["products"]

#to add data, use client to use function: inset_many() or insert_one()
#insert_many() allows to add a list of JSONs, insert_one() allows to add a single JSON

mock_data = [
    {"name": "product 1", "tag": "new", "price":19.99, "image_path": "/static/images/image1.jpg"},
{"name": "product 2", "tag": "old", "price":14.99, "image_path": "/static/images/image2.jpg"},
{"name": "product 3", "tag": "new", "price":24.99, "image_path": "/static/images/image3.jpg"},
{"name": "product 4", "tag": "new", "price":17.99, "image_path": "/static/images/image4.jpg"}
]

# Ran only once, to first insert above data
#products_collection.insert_many(mock_data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)

app.run(host="0.0.0.0", port=5000)
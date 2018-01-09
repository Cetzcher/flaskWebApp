from bson.objectid import ObjectId
from flask import Flask, request, render_template, redirect, jsonify
from flask_bootstrap import Bootstrap  # pip3 install flask-bootstrap
from webapp.model import Database, Item

app = Flask(__name__)
Bootstrap(app)
db = Database(app)


# API routes should return pure json data.
# Use the API routes for the actual page.

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search/<searchstr>')
def search(searchstr):
    # search for the items given and show the item_list page
    return render_template("item_list.html", items=list(db.find_item(searchstr)))


@app.route("/items/all")
def all():
    return render_template("item_list.html", items=list(db.get_all_items()))


@app.route("/items/new", methods=["GET", "POST"])
def create():
    # GET should return the Page.
    # POST to here is the same as PUT to api_items
    # TODO actually create the item or rather dispatch to API call.
    if request.method == "GET":
        return render_template("new_item.html")
    else:
        name = request.form.get("name")
        desc = request.form.get("description")
        url = request.form.get("desc")
        price = request.form.get("price")
        print(name, url, desc, price)
        try:
            if db.get_item(name) is not None:
                raise ValueError("Item already exists")
            elif not name or price == 0:
                raise ValueError("Item needs a name and price > 0")

            price = float(price)

            desc = desc if desc else "No Item description given"
            url = url if url else "http://placehold.it/350x250"
            db.insert_item(Item(name, desc, price, url))
            return redirect("/items/all", 302)
        except ValueError as e:
            return render_template("new_item.html", err=str(e))


@app.route("/items/<string:item>", methods=["GET"])
def item(item):
    # shows a detail view of the item i.e comments, price, buy link etc
    return render_template("item_detail.html", item=db.get_item(item))


@app.route("/items/<string:item>/buy")
def buy(item):
    # disallow GET since items could stop being accessible ?
    return render_template("item_list.html", items=db.get_all_items())


@app.route("/items/<string:item>")
def serve_item(item):
    # show all items in given cat.
    return ""


app.run(port=5000)

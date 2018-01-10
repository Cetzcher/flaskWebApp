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
        url = request.form.get("url")
        price = request.form.get("price")
        try:
            if not name or price == 0:
                raise ValueError("Item needs a name and price > 0")
            elif not db.get_item(name):
                raise NameError("The name of the item is already in use")

            price = float(price)

            desc = desc if desc else "No Item description given"
            url = url if url else "http://placehold.it/350x250"
            db.insert_item(Item(name, desc, price, url))
            return redirect("/items/all", 302)
        except ValueError as e:
            return render_template("err.html", err=str(e))
        except NameError as e:
            return render_template("err.html", err=str(e))


@app.route("/items/<string:item>", methods=["GET", "POST"])
def item(item):
    if request.method == "GET":
        got_item = list(db.get_item(item))[0]
        print(got_item)
        # shows a detail view of the item i.e comments, price, buy link etc
        return render_template("item_detail.html", item=got_item, comments=got_item["comments"])
    else:
        got_item = list(db.get_item(item[1:]))[0]
        username = request.form.get("username")
        content = request.form.get("content")
        try:
            if username in got_item["comments"]:
                raise NameError("Username already in use")
            db.insert_comment(got_item, username, content)
            return redirect("/items/" + item[1:])
        except NameError as e:
            return render_template("err.html", err=str(e))


@app.route("/items/<string:item>/buy")
def buy(item):
    # disallow GET since items could stop being accessible ?
    return render_template("item_list.html", items=db.get_all_items())


app.run(port=5000)

from flask import Flask, request, render_template, redirect, jsonify
from flask_bootstrap import Bootstrap  # pip3 install flask-bootstrap

app = Flask(__name__)
Bootstrap(app)

# API routes should return pure json data.
# Use the API routes for the actual page.

@app.route("/api/search/<string:q>")
def api_search(q):
    return ""


@app.route("/api/items/<string:item>")
def api_serve_category(item):
    # show all items in given cat.
    return ""


@app.route("/api/items/<string:item>/comments")
def api_serve_comments(item):
    # show the comments to that item when GET, when POST create a new one.
    pass


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search/<searchstr>')
def search(searchstr):
    # show the user profile for that user
    return 'User %s' % searchstr


@app.route("/items/all")
def all():
    return render_template("item_list.html")


@app.route("/items/<string:item>")
def serve_item(item):
    # show all items in given cat.
    return ""


@app.route("/items/<string:item>/comments")
def serve_comments(item):
    # show the comments to that item when GET, when POST create a new one.
    pass

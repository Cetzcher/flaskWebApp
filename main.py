from flask import Flask, request, render_template, redirect, jsonify
app = Flask(__name__)

"""
THIS SHOULD ACT AS THE SERVICE URL
FOR THE APPLICATION
"""

class Category:

    LAST_ID = 0

    def __init__(self, name):
        self.id = Category.LAST_ID
        Category.LAST_ID += 1
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item


class Item:

    def __init__(self, name, short_desc, long_desc):
        self.name = name
        self.short = short_desc
        self.long = long_desc
        self.comments = []
        self.rateings = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_rateing(self, rateing):
        self.rateings.append(rateing)

    def score(self):
        i, n = 0, 0
        for rateing in self.rateings:
            i += rateing.val
            n += 1
        return i / n if n > 0 else 0


class Comment:

    def __init__(self, user, text):
        self.user = user
        self.text = text

class Rateing:

    def __init__(self, val):
        self.val = val

DAT = [Category("Initial catagory")] # THIS NEEDS TO BE A DICT


def success(data):
    return jsonify({"success": True, "data": data})


def error(err_msg):
    return jsonify({"success": False, "error": err_msg})



@app.route("/")
def index():
    return render_template("index.html")


# FIELDS FOR POST:
#   catName
@app.route("/api/categories", methods=["GET"])
def categories():
    return success({"Categories": list(map(lambda it: it.name, DAT))}) if request.method == "GET" \
        else error("{0} is unavailable".format(request.method))


@app.route("/api/categories/<string:cat>", methods=["GET", "PUT", "DELETE"])
def detail(cat):
    cats = list(map(lambda it: it.name, DAT))
    if request.method == "GET":
        if cat in cats:
            return success({"items": list(map(lambda it: it.name, DAT[cat].name ))})
    elif request.method == "PUT":
        return success("")
    elif request.method == "DELETE":
        return success("")
    return error("{0} is unssported".format(request.method))


@app.route("/api/categories/<string:cat>/<string:item>", methods=["GET", "POST", "DELETE"])
def item(id, item):
    pass


@app.route("/api/categories/<string:cat>/<string:item>/rate", methods=["GET", "POST"])
def rate(id, item):
    pass


@app.route("/api/categories/<int:id>/<string:item>/comment", methods=["GET", "POST"])
def comment(id, item):
    pass
















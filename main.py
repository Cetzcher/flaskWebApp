from flask import Flask, request, render_template, redirect
app = Flask(__name__)

"""
Paths should look somewhat like this:

GET    /                    index, show all categories                
POST   /                    creates a category.

GET    /<string:cat>        shows overview of that category.
POST   /<cat>               creates a new item.

GET    /<cat>/<string:item> shows a description of the item and links to a rate page

GET    /<cat>/<item>/rate   shows all ratings of an item
POST   /<cat>/<item>/rate   rates an item.

GET    /<cat>/<item>/rate/<int:id>

 
"""

# this is for testing only, should be moved to database interaction.
DATA = {"books": ["LOTR", "The Art of Computer programming"], "games": {}, "movies": {}}


@app.route("/", methods=['GET', "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', cat=DATA.keys())
    elif request.method == "POST":
        cat = request.form["cat"]
        if cat:
            DATA[cat] = []
        else:
            return "CAT = undef"
        return redirect("/", 302)



@app.route('/<string:cat>', methods=["GET", "POST"])
def overview(cat=None):
    if request.method == "GET":
        if cat not in DATA:
            return "Not found"
        return render_template("cat.html", cName=cat, entries=DATA[cat])
    elif request.method == "POST":
        if cat in DATA:
            desc, name = request.form["desc"], request.form["name"]
            DATA[cat] = desc
            return redirect("/" + cat)

        else:
            return "NOT FOUND"

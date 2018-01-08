from flask_pymongo import PyMongo
import re


class Database:

    def __init__(self, app):
        """
        Constructor of the Database class
        It configures the MongoDB connection and initializes a PyMongo object

        :param app: The Flask application
        """
        app.config['MONGO_URI'] = 'mongodb://scupi:sewistcool@ds247027.mlab.com:47027/sew-flask-webapp'
        self.mongo = PyMongo(app)

    def insert_item(self, item):
        """
        Inserts a document that contains information about an item

        :param item: Item class that will be inserted in the database
        :return: None
        """
        self.mongo.db.items.insert_one(item.__dict__)

    def insert_comment(self, comment):
        """
        Inserts a document that contains information about a comment

        :param comment: Comment class that will be inserted in the database
        :return: None
        """
        self.mongo.db.comments.insert_one(comment.__dict__)

    def delete_item(self, name):
        """
        Deletes an item from the web shop that matches with the parameter name

        :param name: The name of the item that will be deleted
        :return: None
        """
        self.mongo.db.items.delete_one(name)

    def delete_comment(self, comment):
        """
        Deletes a comment that matches the comment object given by the parameter

        :param comment: Comment object that will be deleted
        :return: None
        """
        self.mongo.db.comments.delete_one(comment.__dict__)

    def get_all_items(self):
        """
        Gets all the items

        :return: A dictionary with all the items
        """
        return self.mongo.db.items.find()

    def get_all_comments(self):
        """
        Gets all the comments

        :return: A dictionary with all the comments
        """
        return self.mongo.db.comments.find()

    def find_item(self, search_name):
        """
        Copied from https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python and edited to match the web shop

        :param search_name: The searched item
        :return: A list of suggested items
        """
        name_list = map(lambda it: it.get("name"), self.mongo.db.items.find())
        suggestions = []
        pattern = '.*?'.join(search_name)  # Converts 'djm' to 'd.*?j.*?m'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in name_list:
            match = regex.search(item)  # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in sorted(suggestions)]


class Item:

    def __init__(self, name="", description="", price=0.00, pic_url=""):
        """
        Constructor of the Item class

        :param name: The name of the item
        :param description: The description of the item
        :param price: The price of the item
        :param pic_url: The url for the item picture
        """
        self.name = name
        self.description = description
        self.price = price
        self.pic_url = pic_url

    def json_to_txt(self, json_dump):
        """
        Takes a JSON dictionary and gives the values to the attributes

        :param json_dump: JSON dictionary
        :return: None
        """
        self.name = json_dump.get('name')
        self.description = json_dump.get('description')
        self.price = json_dump.get('price')
        self.pic_url = json_dump.get('pic_url')


class Comment:

    def __init__(self, username="", item_name="", description=""):
        """
        Constructor of the Comment class

        :param username: The username of the user who wrote the comment
        :param item_name: The name of the item the comment belongs to
        :param description: The content the user wrote
        """
        self.username = username
        self.item_name = item_name
        self.description = description

    def json_to_txt(self, json_dump):
        """
        Takes a JSON dictionary and gives the values to the attributes

        :param json_dump: JSON dictionary
        :return: None
        """
        self.username = json_dump.get('username')
        self.item_name = json_dump.get('item_name')
        self.description = json_dump.get('description')

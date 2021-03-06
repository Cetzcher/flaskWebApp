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
        if isinstance(item, Item):
            self.mongo.db.items.insert_one(item.__dict__)
        else:
            self.mongo.db.items.insert_one(item)

    def get_item(self, item_name):
        """
        Gets an item

        :param item_name: The name of the item
        :return: The item as a dictionary
        """
        return self.mongo.db.items.find({"name": str(item_name)})

    def insert_comment(self, item, username, content):
        """
        Gets a new item and puts in a new comment then it updates the item

        :param item: The item where the comment belongs
        :param username: The name of the user who wrote the comment
        :param content: Content of the content
        :return: None
        """
        new_item = list(self.get_item(item["name"]))[0]
        new_item["comments"][username] = content
        self.update_item(item["name"], new_item)

    def delete_item(self, name):
        """
        Deletes an item from the web shop that matches with the parameter name

        :param name: The name of the item that will be deleted
        :return: None
        """
        self.mongo.db.items.delete_one(list(self.get_item(name))[0])

    def delete_comment(self, item, username):
        """
        Deletes a comment from an item
        It gets the old item, deletes the comment that matches the username then it updates the item

        :param item: The item the comment belongs to
        :param username: The name of the user who wrote the item
        :return: None
        """
        new_item = list(self.get_item(item["name"]))[0]
        del new_item["comments"][username]
        self.update_item(item["name"], new_item)

    def update_item(self, name, item):
        """
        Updates an item that matches the name given by the parameter

        :param name: The name of the item
        :param item: The new item
        :return: None
        """
        self.delete_item(name)
        self.insert_item(item)

    def update_comment(self, item, new_content, username):
        """
        Updates a comment from an item that matches the given username
        It first gets the item then it changes the comment and updates the item

        :param item: The item which contains the new comment
        :param new_content: The updated comment that will be inserted
        :param username: The name of the user who wrote the comment
        :return: None
        """
        new_item = list(self.get_item(item["name"]))[0]
        new_item["comments"][username] = new_content
        self.update_item(item["name"], new_item)

    def get_all_items(self):
        """
        Gets all the items

        :return: A dictionary with all the items
        """
        return self.mongo.db.items.find()

    def find_item(self, search_name):
        """
        Copied from https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python and edited to match the web shop

        :param search_name: The searched item
        :return: A list of suggested items
        """
        name_dict = {d["name"]: d for d in self.mongo.db.items.find()}
        suggestions = []
        pattern = '.*?'.join(search_name)  # Converts 'djm' to 'd.*?j.*?m'

        regex = re.compile(pattern)  # Compiles a regex.
        for key in name_dict.keys():
            match = regex.search(key)  # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), key))
        return [name_dict[x] for _, _, x in sorted(suggestions)]


class Item:

    def __init__(self, name="", description="", price=0.00, pic_url="", comments={}):
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
        self.comments = comments

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
        self.comments = json_dump.get('comments')

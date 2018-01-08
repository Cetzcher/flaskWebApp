import json


class Item:

    def __init__(self, name="", description="", price=0.00, pic_url="", comments=[]):
        """
        Constructor of the Item class

        :param name:
        :param description:
        :param price:
        :param pic_url:
        :param comments:
        """
        self.name = name
        self.description = description
        self.price = price
        self.pic_url = pic_url
        self.comments = comments

    def txt_to_json(self):
        """
        Text to JSON method
        It generates the content of the method to a dictionary and dumps the dict to a JSON string

        :return: JSON string
        """
        json_dict = {'name': self.name, 'description': self.description, 'price': self.price,
                     'pic_url': self.pic_url, 'comments': self.comments}
        return json.dumps(json_dict, indent=4, separators=(',', ': '))

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


class Comment:

    def __init__(self, username="", description=""):
        """
        Constructor of the Comment class

        :param username: The username of the user who wrote the comment
        :param description: The content the user wrote
        """
        self.username = username
        self.description = description

    def txt_to_json(self):
        """
        Text to JSON method
        It generates the content of the method to a dictionary and dumps the dict to a JSON string

        :return: JSON string
        """
        json_dict = {'username': self.username, 'description': self.description}
        return json.dumps(json_dict, indent=4, separators=(',', ': '))

    def json_to_txt(self, json_dump):
        """
        Takes a JSON dictionary and gives the values to the attributes

        :param json_dump: JSON dictionary
        :return: None
        """
        self.username = json_dump.get('username')
        self.description = json_dump.get('description')

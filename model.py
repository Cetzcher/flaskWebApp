import json


class Item:

    def __init__(self, name="", description="", price=0.00, pic_url=""):
        self.name = name
        self.description = description
        self.price = price
        self.pic_url = pic_url

    def txt_to_json(self):
        json_dict = {'name': self.name, 'description': self.description, 'price': self.price, 'pic_url': self.pic_url}
        return json.dumps(json_dict, indent=4, separators=(',', ': '))

    def json_to_txt(self, json_dump):
        self.name = json_dump.get('name')
        self.description = json_dump.get('description')
        self.price = json_dump.get('price')
        self.pic_url = json_dump.get('pic_url')


class Comment:

    def __init__(self, username="", description=""):
        self.username = username
        self.description = description

    def txt_to_json(self):
        json_dict = {'username': self.username, 'description': self.description}
        return json.dumps(json_dict, indent=4, separators=(',', ': '))

    def json_to_txt(self, json_dump):
        self.username = json_dump.get('username')
        self.description = json_dump.get('description')

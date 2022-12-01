import json


class JSonReader:
    def __init__(self):
        # JSON file
        f = open('./data.json', "r")

        # Reading from file
        self.data = json.loads(f.read())

        # Closing file
        f.close()

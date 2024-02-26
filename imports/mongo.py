from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host, port):
        self.client = MongoClient(host, port)
        self.db = self.client["libfinal"]
        self.books_collection = self.db["books"]
        self.customers_collection = self.db["customers"]


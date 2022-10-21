from tinydb import TinyDB, Query
from common.constants import Constants

class DBHandler:
    def __init__(self):
        self.db = TinyDB(Constants().DB)

    def create_class(self, obj):
        print("Hello world")

    def update_class(self, name, obj):
        print("Hello world")

    def delete_class(self, name):
        print("Hello world")

    def get_class(self, name):
        print("Hello world")

    def get_classes(self):
        print("Hello world")

    def create_reminder(self, obj):
        print("Hello world")

    def update_reminder(self, id, obj):
        print("Hello world")

    def delete_reminder(self, id):
        print("Hello world")

    def get_reminder(self, id):
        print("Hello world")

    def get_reminders(self):
        print("Hello world")

    

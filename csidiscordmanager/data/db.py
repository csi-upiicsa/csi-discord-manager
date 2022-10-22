from tinydb import TinyDB, Query
from csidiscordmanager.common.constants import Constants

class DBHandler:
    def __init__(self):
        self.db = TinyDB(Constants().DB)

    def create_class(self, obj):
        # Crear una clase
        print("Hello world")

    def update_class(self, id, obj):
        # Cambiar/Actualizar una clase
        print("Hello world")

    def delete_class(self, id):
        # Borrar una clase
        print("Hello world")

    def get_class(self, id):
        # Buscar reminder por id
        print("Hello world")

    def get_classes(self):
        # Ver todas las clases
        print("Hello world")

    def create_reminder(self, obj):
        # Crear un reminder
        print("Hello world")

    def update_reminder(self, id, obj):
        # Cambiar/Actualizar un reminder
        print("Hello world")

    def delete_reminder(self, id):
        # Borrar un reminder
        print("Hello world")

    def get_reminder(self, id):
        # Buscar reminder por id
        print("Hello world")

    def get_reminders(self):
        # Ver todos los reminders
        print("Hello world")

    

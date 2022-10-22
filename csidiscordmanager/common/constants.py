import os
from dotenv import load_dotenv
from pathlib import Path

class Constants:
    def __init__(self):
        load_dotenv('.env')
        self.DB = os.getenv('DB')
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')
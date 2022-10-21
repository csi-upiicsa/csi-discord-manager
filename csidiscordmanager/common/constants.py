import os
from dotenv import load_dotenv
from pathlib import Path

class Constants:
    def __init__(self):
        dotenv_path = Path('../../.env')
        load_dotenv(dotenv_path=dotenv_path)
        self.DB = os.getenv('DB')
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')
import os

from dotenv import load_dotenv
from supabase import create_client


class ConnectionLakehouse:
    def __init__(self):
        load_dotenv()
        self.LAKEHOUSE_URL = os.getenv('LAKEHOUSE_URL')
        self.LAKEHOUSE_KEY = os.getenv('LAKEHOUSE_KEY')

    def create_connection(self):
        return create_client(self.LAKEHOUSE_URL, self.LAKEHOUSE_KEY)

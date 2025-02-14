from supabase import create_async_client
from dotenv import load_dotenv
import os


class ConnectionLakehouse():
    def __init__(self):
        load_dotenv()
        self.LAKEHOUSE_URL = os.getenv("LAKEHOUSE_URL")
        self.LAKEHOUSE_KEY = os.getenv("LAKEHOUSE_KEY")
        
    async def create_connection(self):
        return create_async_client(self.LAKEHOUSE_URL, self.LAKEHOUSE_KEY)

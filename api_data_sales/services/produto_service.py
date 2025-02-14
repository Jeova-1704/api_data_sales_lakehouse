import pandas as pd

from api_data_sales.config.settings import ConnectionLakehouse

SCHEMA = 'gold'
TABLE_NAME = 'analise_produtos'


class ProdutoService:
    def __init__(self):
        self.df = self.__get_data()

    def __get_data(self):
        connection = ConnectionLakehouse()
        client = connection.create_connection()
        response = (
            client.schema(SCHEMA).table(TABLE_NAME).select('*').execute()
        )

        return pd.DataFrame(response.data)

    def list_all_categories(self):
        if self.df.empty:
            return []

        categories = list(self.df['categoria'].dropna().unique())
        return categories

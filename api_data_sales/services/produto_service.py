import pandas as pd
from dotenv import load_dotenv
import os

from api_data_sales.config.settings import ConnectionLakehouse
from api_data_sales.models.product_schema import TotalSoldCategory


class ProdutoService:
    def __init__(self):
        load_dotenv()
        self.schema = os.getenv('SCHEMA')
        self.table_name = os.getenv('TABLE_PRODUCT_NAME')
        self.df = self.__get_data()

    def __get_data(self):
        connection = ConnectionLakehouse()
        client = connection.create_connection()

        all_data = []
        offset = 0
        batch_size = 10_000

        while True:
            try:
                response = (
                    client.schema(self.schema)
                    .table(self.table_name)
                    .select('*')
                    .range(offset, offset + batch_size - 1)
                    .execute()
                )
                batch_data = response.data

                if not batch_data:
                    break

                all_data.extend(batch_data)
                offset += batch_size

            except Exception as e:
                break

        return pd.DataFrame(all_data)

    def list_all_categories(self):
        if self.df.empty:
            return []

        categories = list(self.df['categoria'].dropna().unique())
        return categories

    def quantity_product(self):
        quantity = self.df.shape[0]
        return quantity
    
    def quantity_category(self):
        quantity = self.df['categoria'].nunique()
        return quantity
    
    def get_total_products_sold(self):
        quantity = self.df['total_vendido'].sum()
        return quantity
    
    def get_total_sold_by_category(self):
        if self.df.empty or 'categoria' not in self.df.columns or 'total_vendido' not in self.df.columns:
            return []  # Retorna lista vazia se não houver dados válidos

        grouped = self.df.groupby('categoria')['total_vendido'].sum().reset_index()

        # Convertendo para a estrutura esperada
        result = [TotalSoldCategory(category=row['categoria'], quantity=int(row['total_vendido'])) for _, row in grouped.iterrows()]

        return result
import os

import pandas as pd
from dotenv import load_dotenv

from api_data_sales.config.settings import ConnectionLakehouse


class ClientesPedidosServices:
    def __init__(self):
        load_dotenv()
        self.schema = os.getenv('SCHEMA')
        self.table_name = os.getenv('TABLE_CLIENTE_PEDIDO')
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

            except Exception:
                break

        return pd.DataFrame(all_data)

    def get_avg_age(self):
        quantity_data = self.df.shape[0]
        sum_age = self.df['idade'].sum()
        return round((sum_age / quantity_data), 2)

    def get_total_value(self):
        total_gasto = self.df['total_gasto'].sum()
        return round(total_gasto, 2)
    
    def get_total_order(self):
        total_pedido = self.df['total_pedido'].sum()
        return round(total_pedido, 2)
    
    def get_avg_order(self):
        quantity_data = self.df.shape[0]
        sum_order = self.df['total_pedido'].sum()
        return round((sum_order / quantity_data), 2)

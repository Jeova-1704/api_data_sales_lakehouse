from fastapi import FastAPI

from api_data_sales.routers.produto_router import router as products_router

app = FastAPI(title='Data lakehouse API', version='1.0.0')

app.include_router(products_router, prefix='/api')

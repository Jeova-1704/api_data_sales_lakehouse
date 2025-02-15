from http import HTTPStatus

from fastapi import APIRouter

from api_data_sales.models.product_schema import (
    CategoryList,
    QuantityResponse,
    TotalQuantityByCategory,
)
from api_data_sales.services.produto_service import ProdutoService

router = APIRouter(prefix='/products')
product_service = ProdutoService()


@router.get(
    '/categories', status_code=HTTPStatus.OK, response_model=CategoryList
)
def get_all_categories():
    categories = product_service.list_all_categories()
    return {'categories': categories}


@router.get(
    '/quantity-products',
    status_code=HTTPStatus.OK,
    response_model=QuantityResponse,
)
def get_quantity_products():
    quantity = product_service.quantity_product()
    return {'quantity': quantity}


@router.get(
    '/quantity-category',
    status_code=HTTPStatus.OK,
    response_model=QuantityResponse,
)
def get_quantity_products():
    quantity = product_service.quantity_category()
    return {'quantity': quantity}


@router.get(
    '/quantity-products-sold',
    status_code=HTTPStatus.OK,
    response_model=QuantityResponse,
)
def get_quantity_products_sold():
    quantity = product_service.get_total_products_sold()
    return {'quantity': quantity}


@router.get(
    '/total-sold-by-category',
    status_code=HTTPStatus.OK,
    response_model=TotalQuantityByCategory,
)
def get_total_sold_by_category():
    result = product_service.get_total_sold_by_category()
    return {'data': result}


@router.get(
    '/total-recipe', status_code=HTTPStatus.OK, response_model=QuantityResponse
)
def get_total_recipe():
    quantity = product_service.get_total_recipe()
    return {'quantity': quantity}


@router.get(
    '/total-stock', status_code=HTTPStatus.OK, response_model=QuantityResponse
)
def get_total_stock():
    quantity = product_service.get_total_stock()
    return {'quantity': quantity}


@router.get(
    '/total-stock-by-category',
    status_code=HTTPStatus.OK,
    response_model=TotalQuantityByCategory,
)
def get_total_sold_by_category():
    result = product_service.get_total_stock_by_category()
    return {'data': result}

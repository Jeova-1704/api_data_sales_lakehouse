from http import HTTPStatus

from fastapi import APIRouter

from api_data_sales.models.product_schema import CategoryList
from api_data_sales.services.produto_service import ProdutoService

router = APIRouter(prefix='/products')
product_service = ProdutoService()


@router.get(
    '/categories', status_code=HTTPStatus.OK, response_model=CategoryList
)
def get_all_categories():
    categories = product_service.list_all_categories()
    return {'categories': categories}

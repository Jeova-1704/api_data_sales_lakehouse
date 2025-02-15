from http import HTTPStatus

from fastapi import APIRouter
from api_data_sales.services.clientes_pedidos_service import (
    ClientesPedidosServices,
)
from api_data_sales.models.clientes_pedidos_schema import QuantityFloatResponse


router = APIRouter(prefix='/cliente-pedido')
client_order_service = ClientesPedidosServices()


@router.get(
    '/avg-age', status_code=HTTPStatus.OK, response_model=QuantityFloatResponse
)
def get_all_categories():
    quantity = ClientesPedidosServices.get_avg_age()
    return {'quantity': quantity}


@router.get(
    '/total-value',
    status_code=HTTPStatus.OK,
    response_model=QuantityFloatResponse,
)
def get_total_values():
    quantity = ClientesPedidosServices.get_total_value()
    return {'quantity': quantity}


@router.get(
    '/total-pedido',
    status_code=HTTPStatus.OK,
    response_model=QuantityFloatResponse,
)
def get_total_order():
    quantity = ClientesPedidosServices.get_total_order()
    return {'quantity': quantity}


@router.get(
    '/avg-total-order',
    status_code=HTTPStatus.OK,
    response_model=QuantityFloatResponse,
)
def get_avg_order():
    quantity = ClientesPedidosServices.get_avg_order()
    return {'quantity': quantity}

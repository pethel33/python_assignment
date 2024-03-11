from fastapi import APIRouter, Depends

from schema.order import Order, OrderCreate, OrderStatus, orders
from services.order import order_service

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get curr order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids,
    )
    orders.append(new_order)
    return {'message': 'Order created successfully', 'data': new_order}

@order_router.put('/process_order/{order_id}', status_code=201)
def process_order(order_id: int = Depends(order_service.does_order_exist)):
    for order in orders:
        if order.id == order_id:
            order.status = OrderStatus.completed.value
            # response = order_service.order_parser([order])
            # response = order_service.order_parser([order])

            # return {'message': 'successful', 'status': order.status, 'data': response[0].items}
            return {'message': 'successful', 'data': order}




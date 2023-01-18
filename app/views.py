from flask import jsonify, request

from app import app
from app.db import engine, Session
from app.db.models import User, Offer, Order

def get_user_list(users):
    user_list = []
    for user in  users:
        add_user = User(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
            )
        user_list.append(add_user)
    return user_list


def get_order_list(orders):
    order_list = []
    for order in orders:
        add_order = Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=order['start_date'],
            end_date=order['end_date'],
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
            )
        order_list.append(add_order)
    return order_list


def get_offer_list(offers):
    offer_list = []
    for offer in offers:
        add_offer = Offer(
            id=offer('id'),
            order_id=offer('order_id'),
            executor_id=offer('executor_id')
            )
        offer_list.append(add_offer)
    return offer_list


@app.route('/users/')  # , methods=['GET', 'POST'])
def get_users():
    with Session() as engine_session:
        users = session.query(User).all()
    result = []

    for user in users:
        result.append(user.get_user())
    return jsonify(result)


@app.route('/users/<int:id>')
def users_id(id):
    with Session() as engine_session:
        users = engine_session.query(User).get(id)

    if users is None:
        return 'User is not found'
    return jsonify(users.get_user())


@app.route('/orders/')
def get_orders():
    with Session() as engine_session:
        orders = engine_session.query(Order).all()
    result = []

    for order in orders:
        result.append(order.get_order())
    return jsonify(result)


@app.route('/orders/<int:id>')
def orders_id(id):
    with Session() as engine_session:
        orders = engine_session.query(Order).get(id)
    if orders is None:
        return 'User is not found'
    return jsonify(orders.get_order())


@app.route('/offers/')
def get_offers():
    with Session() as engine_session:
        offers = engine_session.query(Offer).all()
    result = []

    for offer in offers:
        result.append(offer.get_offer())
    return jsonify(result)


@app.route('/offers/<int:id>')
def offers_id(id):
    with Session() as engine_session:
        offers = engine_session.query(Offer).get(id)
    if offers is None:
        return 'User is not found'
    return jsonify(offers.get_offer())


@app.route('/users/', methods=['POST'])
def add_user():
    data = request.json
    try:
        add_user = User(
            id=data.get('id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age'),
            email=data.get('email'),
            role=data.get('role'),
            phone=data.get('phone')
        )
        with Session() as engine_session:
            engine_session.add(add_user)
            engine_session.commit()
        return 'Users add'
    except IntegrityError as e:
        return 'User exist'


@app.route('/users/<int:id>', methods=['PUT'])
def update_user_id(id):
    data = request.json
    with Session() as engine_session:
        user = engine_session.query(User).get(id)
        if user is None:
            return 'User is not found'
        user.id = data.get('id')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.age = data.get('age')
        user.email = data.get('email')
        user.role = data.get('role')
        user.phone = data.get('phone')
        engine_session.add(user)
        engine_session.commit()
    return f'User {id} update'


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_id(id):
    with Session() as engine_session:
        user = engine_session.query(User).get(id)
        if user is None:
            return 'User is not found'
        engine_session.delete(user)
        engine_session.commit()
        return f'User {id} deleted'


@app.route('/orders/', methods=['POST'])
def add_order():
    data = request.json
    try:
        add_order = Order(
            id=data.get('id'),
            name=data.get('name'),
            description = data.get('description'),
            start_date = data.get('start_date'),
            end_date = data.get('end_date'),
            address = data.get('address'),
            price = data.get('price'),
            customer_id = data.get('customer_id'),
            executor_id = data.get('executor_id')
        )
        with Session() as engine_session:
            engine_session.add(add_order)
            engine_session.commit()
        return 'Order add'
    except IntegrityError as e:
        return 'Order exist'


@app.route('/orders/<int:id>', methods=['PUT'])
def update_order_id(id):
    data = request.json
    with Session() as engine_session:
        order = Order.query.get(id)
        if order is None:
            return 'Order is not found'
        order.id = data.get('id')
        order.name = data.get('name')
        order.description = data.get('description')
        order.start_date = data.get('start_date')
        order.end_date = data.get('end_date')
        order.address = data.get('address')
        order.price = data.get('price')
        order.customer_id = data.get('customer_id')
        order.executor_id = data.get('executor_id')
        engine_session.add(order)
        engine_session.commit()
    return f'Order {id} update'


@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_orders_id(id):
    with Session() as engine_session:
        order = engine_session.query(Order).get(id)
        if order is None:
            return 'Order is not found'
        engine_session.delete(order)
        engine_session.commit()
    return f'Order {id} deleted'


@app.route('/offers/', methods=['POST'])
def add_offer():
    data = request.json
    try:
        add_offer = Offer(
            id=data.get('id'),
            order_id=data.get('order_id'),
            executor_id = data.get('executor_id')
        )
        with Session() as engine_session:
            engine_session.add(add_offer)
            engine_session.commit()
        return 'Offer add'
    except IntegrityError as e:
        return 'Offer exist'


@app.route('/offers/<int:id>', methods=['PUT'])
def update_offer_id(id):
    data = request.json
    with Session() as engine_session:
        offer = engine_session.query(Offer).get(id)
        if offer is None:
            return 'Offer is not found'
        offer.id = data.get('id')
        offer.order_id = data.get('order_id')
        offer.executor_id = data.get('executor_id')
        engine_session.add(offer)
        engine_session.commit()
    return f'Offer {id} update'


@app.route('/offers/<int:id>', methods=['DELETE'])
def delete_offer_id(id):
    with Session() as engine_session:
        offer = engine_session.query(Offer).get(id)
        if offer is None:
            return 'Order is not found'
        engine_session.delete(offer)
        engine_session.commit()
    return f'Offer {id} deleted'

from app import db

import sqlalchemy as sa


class User(db.Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    email = sa.Column(sa.String)
    role = sa.Column(sa.String)
    phone = sa.Column(sa.String)

    def get_user(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone
        }


class Order(db.Base):
    __tablename__ = "order"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)
    start_date = sa.Column(sa.String)
    end_date = sa.Column(sa.String)
    address = sa.Column(sa.String)
    price = sa.Column(sa.Integer)
    customer_id = sa.Column(sa.Integer)
    executor_id = sa.Column(sa.Integer)

    def get_order(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price,
            'customer_id': self.customer_id,
            'executor_id': self.executor_id
        }


class Offer(db.Base):
    __tablename__ = "offer"
    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer)
    executor_id = sa.Column(sa.Integer)

    def get_offer(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id
        }

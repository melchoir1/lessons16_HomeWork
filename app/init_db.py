import json
import os

import sqlalchemy
from app.db import engine, Base
from app.db.models import User, Order, Offer


class GetData:

    @staticmethod
    def load_json(file_name):
        with open(file_name, encoding='UTF-8') as file:
            return json.load(file)


    def create_db(self):
        filePath = 'project.db'
        
        if os.path.exists(filePath):
            print("base already exists")
            os.remove(filePath)

        print("create schema")
        Base.metadata.create_all(engine)

        with sqlalchemy.orm.Session(engine) as session:

            users = self.load_json(os.path.join('data', 'users.json'))
            orders = self.load_json(os.path.join('data', 'orders.json'))
            offers = self.load_json(os.path.join('data', 'offers.json'))
            print("load users")
            self.add_data(users, User, session)
            print("load orders")
            self.add_data(orders, Order, session)
            print("load offers")
            self.add_data(offers, Offer, session)

            session.commit()

    @staticmethod
    def add_data(json_data, model, session):
        for item in json_data:
            unit = model(**item)
            session.add(unit)


def init_db():
    GetData().create_db()

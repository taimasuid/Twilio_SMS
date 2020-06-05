from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey, BigInteger)
from run import db


class User(db.Model):

    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50))
    password = Column('password', String(200))
    phone = Column('phone', String(20))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):

    __tablename__ = "products"

    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    message = Column('message', String(200))


class Order(db.Model):

    __tablename__ = "orders"

    id = Column('id', Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_phone = Column('customer_phone', String(15))
    shipped = Column('shipped', Boolean())


if __name__ == "__main__":
    db.create_all()

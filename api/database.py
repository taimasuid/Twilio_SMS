from run import db
from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey)


class Users(db.Model):

    __tablename__ = "users"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50))
    phone = Column('phone', String(20))

    def __repr__(self):
        return '<Users {}>'.format(self.username)

class Orders(db.Model):

    __tablename__ = "orders"

    id = Column('id', Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_phone = Column('customer_phone', String(15))
    shipped = Column('shipped', Boolean())

class Products(db.Model):

    __tablename__ = "products"

    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column('message', String(200))




if __name__ == "__main__":
    db.create_all()

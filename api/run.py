""" The main Flask application file that bootstraps and starts the app. """

import os
from flask import (
    flash, g, redirect, render_template, request, session, url_for, sessions
)
from flask_migrate import Migrate
from twilio.rest import Client

from bootstrap import app_factory, database_factory


app = app_factory()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
print(app.config['SECRET_KEY'])
print(app.config['SQLALCHEMY_DATABASE_URI'])
with app.app_context():
    db = app.db
    db.drop_all()
    migrate = Migrate(app, db)


from models import User, Product, Order


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        error = None
        print(username, password, phone)

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        user = User.query.filter_by(username=username).first()
        if user:
            error = 'User {} already exists'.format(username)

        if error is None:
            user = User(username=username, password=password, phone=phone)
            db.session.add(user)
            db.session.commit()

            session['username'] = username
            print("user added")
            return redirect(url_for('login'))
        flash(error)

    return render_template('registration.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif password != user.password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['username'] = username
            username = session.get('username')
            if username is None:
                g.user = None
            else:
                g.user = User.query.filter_by(username=username).first()
            print('logging user')
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')


account_sid = os.environ.get("SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_from = os.environ.get('TWILIO_FROM')


@app.route('/index',  methods=['GET', 'POST'])
def index():
    username = session.get('username')
    print(username)
    user = User.query.filter_by(username=username).first()
    products = Product.query.filter_by(user_id=user.id).all()
    print(products)
    orders = []
    for prod in products:
        order = Order.query.filter_by(product_id=prod.id).all()
        orders.extend(order)
        print(order)

    if request.method == 'POST':
        if request.form.get('prod_search'):
            prod_id = int(request.form.get('prod_search'))
            products = Product.query.filter_by(id=prod_id).all()
            orders = Order.query.filter_by(product_id=prod_id)

            return render_template('home.html', user=user, products=products, orders=orders)

        if request.form.get('message'):
            message = request.form.get('message')
            add_products(user_id=user.id, message=message)
        if request.form.get('new_message'):
            new_message = request.form.get('new_message')
            prod_id = request.form.get('prod_id')
            prod = Product.query.filter_by(id=prod_id).first()
            prod.message = new_message
            db.session.commit()
        if request.form.get('pid'):
            prod_id = request.form.get('pid')
            customer_phone = request.form.get('cust_phone')
            order = Order(product_id=int(prod_id), customer_phone=customer_phone, shipped=False)
            db.session.add(order)
            db.session.commit()
        if request.form.get('send_shipped'):
            order_id = int(request.form.get('order_id'))
            order = Order.query.filter_by(id=order_id).first()
            product = Product.query.filter_by(id=order.product_id).first()
            phone = order.customer_phone
            try:
                client.messages.create(
                    body=product.message,
                    from_=twilio_from,
                    to='+1' + phone
                )
                flash("Message sent")
            except Exception as e:
                flash('Twilio request failed {}'.format(e))

            order.shipped = True
            db.session.commit()

    return render_template('home.html', user=user, products=products, orders=orders)


def add_products(user_id, message):
    product = Product(user_id=user_id, message=message)
    db.session.add(product)
    db.session.commit()
    print("product {} added".format(product))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))

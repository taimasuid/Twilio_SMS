""" The main Flask application file that bootstraps and starts the app. """

import os
from twilio.rest import Client
# from flask_migrate import Migrate
from flask import flash, g
from flask import request, render_template, url_for, redirect, session
from bootstrap import app_factory, database_factory

#flask
app = app_factory()
#flask config
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postscript:dev@db/postscript'

#import tables
from database import User, Product, Order
#connect to twilio/might want to add to docker-compose.yml in future
ACCOUNT_SID = 'ACebc012a717e6ae5de9a0e71a77b66720'
TWILIO_AUTH_TOKEN = '2f4fa14781f70de5957f1d33b6e32979'
TWILIO_NUMBER= +18187489426
client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN) 


@app.route('/index',  methods=['GET', 'POST'])
def index():

    username = request.form['username']
    if not username:
            error = 'Username is required'
    
    user = User.query.filter_by(username=username).first()

    username = session.get('username')
    print(username)
    #query.filters by username from above
    user = Users.query.filter_by(username=username).first()
    #products avaible for certain users show
    products = Products.query.filter_by(user_id=user.id).all()
    print(products)
    orders = []

    for prod in products:
        order = Orders.query.filter_by(product_id=prod.id).all()
        #all orders info (id ,product_id,customer_phone,shipped) added to orders[]
        orders.extend(order)

    if request.method == 'POST':
         # HTTP Method POST, form was submitted by a user
        if request.form.get('prod_search'):
            #gets product info from user search
            prod_id = int(request.form.get('prod_search'))
            #get products from db for this user
            products = Products.query.filter_by(id=prod_id).all()
            #prod_id is matched to product_id from db to get correct product order
            orders = Orders.query.filter_by(product_id=prod_id)

            return render_template('homepage.html', user=user, products=products, orders=orders)


        #users add message
        if request.form.get('message'):
            new_message = request.form.get('message')
            prod_id = request.form.get('prod_id')
            prod = Products.query.filter_by(id=prod_id).first()
            prod.message = new_message
            products.add(user_id=user.id, message=message)
            db.session.commit()

        #send notifictaion
        if request.form.get('notify'):
            order_id = int(request.form.get('order_id'))
            order = Orders.query.filter_by(id=order_id, shipped=False).first()
            product = Products.query.filter_by(id=order.product_id).first()

            try:
                #create message
                client.messages.create(
                    from_=os.environ.get('TWILIO_NUMBER'),
                    to='+1' + order.customer_phone,
                    body=product.message
                )
                flash("SMS Notifictaion is now sent! :)", "success")
            except Exception as e:
                flash('ERROR: request failed. Try again. :('.format(e), "danger")

            #after sms is sent set order shipped to true
            order.shipped = True 
            db.session.commit()

    return render_template('homepage.html', user=user, products=products, orders=orders)


@app.route("/health-check")
def health_check():
    return {"success": True}


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))

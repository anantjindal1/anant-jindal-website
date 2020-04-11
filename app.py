from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import os
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Restaurant, MenuItem

'''
#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
'''

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def showHome():
    return render_template('index.html')

'''
@app.route('/projects/')
def allProjects():
    return render_template('works.html')

@app.route('/quote/')
def quotes():
    return render_template('get-quote.html')

@app.route('/gallery/')
def photoGallery():
    return render_template('photogallery.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/Equipment/<string:eqtype>/')
def showEquipment(eqtype):
    return render_template('equipments.html',eqtype=eqtype)   #eqtype - "all"/"bridge"/"road"
'''


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

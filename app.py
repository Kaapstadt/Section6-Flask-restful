from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #find in the root
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turns off flask sqlalchamy mofification tracker
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'brian'
api = Api(app)

#flask decorator
@app.before_first_request
def create_tables():
	db.create_all() # if you don't import store and storelist then sqlalchemy won't create the tables
	

jwt =  JWT(app,authenticate,identity) #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item,'/item/<string:name>') 
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')


if __name__ == "__main__":
	db.init_app(app)
	app.run(host='0.0.0.0', port=5000,debug=True)
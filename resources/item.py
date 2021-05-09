from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type = float,
            required = True,
            help = "This field cannot be blank!"

        ) 
    parser.add_argument('store_id',
            type = int,
            required = True,
            help = "Every item needs a store id."

        ) 

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name) :
        if ItemModel.find_by_name(name):
            return{'message':"An item with name '{}' already exist.".format(name)}, 400
        
        data = Item.parser.parse_args()

        #item = ItemModel(name, data['price'], data['store_id']) OR
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return{'message':'An error has occurred inserting item.'}, 500 #Internal server error
        return item.json(),201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}
       
    def put(self,name):
        #data = request.get_json()
        data = Item.parser.parse_args() # check that only price is in the json payload
        item = ItemModel.find_by_name(name)
        
        
        #item =  next(filter(lambda x:x['name'] == name,items),None)
        if item is None:
            #item = ItemModel(name, data['price'], data['store_id']) OR
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            item.store_id = data['store_id'] #optional
        
        item.save_to_db()
           
        return item.json()

class ItemList(Resource):
    def get(self):
        return{'items': [item.json() for item in ItemModel.query.all()]} #list comprehension OR
        #return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))}
       

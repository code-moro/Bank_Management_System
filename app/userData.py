from typing import Collection

from pymongo import collation, collection
from config import DATABASE, client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
from flask.helpers import make_response
from flask.wrappers import Request
import random


Collection = DATABASE['Bank']


@app.route('/checking')
def hello_world():
    message = {
        "code": 200,
        "status": "Application is Working fine"
    }
    res = make_response(jsonify(message), 200)
    return res


@app.route('/createuser', methods=["POST"])
def add_user():
    user = request.get_json()

    if not Collection.find_one({'Mobile_No': user['Mobile_No']}):

        account_no = random.randint(100, 1000)
        
        record={
            '_id': account_no, 
            'Name': user['Name'], 
            'Add': user['Add'], 
            'Mobile_No': user['Mobile_No'], 
            'city': user['city']
            }
        
        Collection.insert_one(record)
        
        res = make_response(jsonify({"Msg": "Record Created", "Account_No": account_no}), 201)
       
        return res
    else:
        res = make_response(jsonify({"Msg": "Phone Number Already Exist"}), 200)
        
        return res


@app.route('/finduser/<id>')
def get_user(id):

    display_user = Collection.find_one({"_id": int(id)}, {"_id": 0})
    
    if display_user:
       
        res = make_response(jsonify({"Msg": "Record Found", "Info": display_user}), 200)
        
        return res
    else:
        res = make_response(jsonify({"Msg": "Record Not Found PLzz create the record"}), 404)
        
        return res


@app.route('/deleteuser/<id>', methods=['DELETE'])
def delete_user(id):
    
    check_rec = Collection.find_one({"_id": int(id)})
    
    if check_rec:
        
        Collection.delete_one({"_id": int(id)})
        
        res = make_response(jsonify({"Msg": "Record deleted successfully"}), 200)
        
        return res
    else:
        
        res = make_response(jsonify({"Msg": "Record Not Found "}), 404)
        
        return res


@app.route('/updateuser/<id>', methods=['PUT'])
def delete_username(id):
    
    check_rec = Collection.find_one({"_id":int(id)})
    req=request.get_json()
    if check_rec:
        
        Collection.update_one({"_id":int(id)},{"$set":req})
        
        res = make_response(jsonify({"Msg": "Record update successfully"}), 202)
        
        return res
    else:
        
        res = make_response(jsonify({"Msg": "Record Not Found"}), 404)
        
        return res

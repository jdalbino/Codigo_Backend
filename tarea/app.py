from ast import Pass
from crypt import methods
from email import message
from http.client import USE_PROXY
from turtle import position
from flask import Flask, request
from flask_cors import CORS, cross_origin
from datetime import datetime

app = Flask(__name__)

CORS(app=app,origins='*',methods='*', allow_headers=['Content-Type'])

users = [
{
"name": "admin",
"lastname": "admin",
"country": "country 1",
"description": "description 1",
"photo": "photo 1",
"cellphone": "cellphone 1",
"TaxPayer": "admin",
"Password": "123",
"email": "admin@gmail.com",
"username": "admin",
"id": 1,
},
{
"name": "name 2",
"lastname": "lastname 2",
"country": "country 2",
"description": "description 2",
"photo": "photo 2",
"cellphone": "cellphone 2",
"TaxPayer": "TaxPayer 2",
"Password": "Password 2",
"email": "email 2",
"username": "username 2",
"id": 2,
},
{
"name": "name 3",
"lastname": "lastname 3",
"country": "country 3",
"description": "description 3",
"photo": "photo 3",
"cellphone": "cellphone 3",
"TaxPayer": "TaxPayer 3",
"Password": "Password 3",
"email": "email 3",
"username": "username 3",
"id": 3,
},
{
"name": "name 4",
"lastname": "lastname 4",
"country": "country 4",
"description": "description 4",
"photo": "photo 4",
"cellphone": "cellphone 4",
"TaxPayer": "TaxPayer 4",
"Password": "Password 4",
"email": "email 4",
"username": "username 4",
"id": 4
}
]

def find_user(id):
    for userposition in range(0,len(users)):
        user = users[userposition]
        if user.get('id') == id:
            return (user,userposition)

# GENERAL SERVER ROUTE
@app.route('/')
@cross_origin()
def runapp():

    hora_del_servidor = datetime.now()
    return {
            'status': True,
            'message':'Server is up and running',
            'hour': hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S'),
        }

# GET RESPONSE AND POST RESPONSE
@app.route('/users',methods=['GET','POST'])
@cross_origin()
def getusers():
    if request.method=='GET':
        return {
        'message':'Available Users',
        'users': users
        }
    elif request.method=='POST':
        data = request.get_json()
        data['id']= len(users)+1
        users.append(data)

        print('request:',request.get_json())
        return {
            'message':'User Created Successfuly',
            'users':data
        }

# GET,PUT,DELETE RESPONSE BY ID
@app.route('/user/<int:id>',methods=['GET','PUT','DELETE'])
@cross_origin()
def getuser(id):
    
    if request.method == 'GET':
       userreq = find_user(id)
       if userreq:
          return userreq[0]
       else:
           return {
           'message':'User not found'
           },404
    elif request.method == 'PUT':
        userreq = find_user(id)
        if userreq:
            [user,userposition] = userreq
            data = request.get_json()
            data['id']= id
            users[userposition]= data
            return users[userposition]
        else:
           return {
           'message':'User to be Updated not found'
           },404
    elif request.method == 'DELETE':
        userreq = find_user(id)
        if userreq:
            [user,userposition] = userreq
            user_eliminado = users.pop(userposition)
            return {
           'message':'User Successfuly eliminated',
           'user':user_eliminado
           }
        else:
           return {
           'message':'User to be Eliminated was not found'
           },404

app.run(host='0.0.0.0',port=8080)


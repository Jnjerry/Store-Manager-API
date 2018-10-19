from flask import jsonify,json,Flask,request,session,redirect,url_for
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
from flask import Flask, request, jsonify,Blueprint

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ngugijoan'
app.config['JWT_SECRET_KEY'] = 'ngugijoan'
jwt = JWTManager(app)

app = Blueprint('auth', __name__,url_prefix='/api/v1/auth')

@app.route("signup", methods=['POST'])#signup endpoint
def signup():
    """route for signup for user"""
    data = request.get_json()
    username = data["username"]
    if username in user_details:
        return jsonify({"message":"username already taken choosen another username"})
    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]
    password = data["password"]
    cpassword = data["cpassword"]
    user_details.update({"username":username, "fname":fname, "lname":lname,\
                          "email" :email, "password":password, "cpassword":cpassword})
                          return jsonify({"message" : "successful signup"})
    response.status_code=201
    return response




@app.route("login", methods=['POST'])#login endpoint
def login():
    """route for login for an activated account"""
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200




@app.route('/user/<name>', methods=['GET'])#guest/admin endpoint
def know_user(name):
    """route to detremine whether you are admin or store attendant """
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

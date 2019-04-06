from flask import Flask, render_template, request, session, jsonify, redirect, url_for, jsonify, make_response
import datetime
import model as database
from flask_cors import CORS, cross_origin
import jwt
from functools import wraps


app = Flask(__name__)
cors = CORS(app)


# when user open site / or open slash the function below it executes
# decorater
# jsonify display in json format

app.secret_key = 'any randomstring'


# @app.route('/pupies/<int:id>/',methods =['GET','POST','DELETE'])
# def home():
#     return render_template('index.html')

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token')
        try:
            data=jwt.decode(token,app.secret_key)

        except:
            return jsonify({'message ': 'invalid'}),403
        return f(*args,**kwargs)
    return decorated



# http://127.0.0.1:5000/blogdata?token=
@app.route('/blogdata', methods=['GET', 'POST', 'DELETE'])
@token_required
def blogdata():
    blog = database.Blog()
    blogs = blog.blog_data()
    return jsonify(blogs)


@app.route('/login', methods=['GET', 'POST', 'DELETE'])
def login():
    
   
    token = jwt.encode({ 'exp': datetime.datetime.utcnow(
    )+datetime.timedelta(minutes=30)}, app.secret_key)
    return jsonify({'token': token.decode('UTF-8')})
    # return make_response('could not verify', 401, {'required': 'token required'})


@app.route('/json', methods=['GET', 'POST', 'DELETE'])
def json():
    return jsonify([1, 'whabh', 'jnjn'])


if __name__ == '__main__':

    app.run(debug=True)
'''
@app.route("/getPics")
def pics():
    return jsonify(shopsPics)
'''

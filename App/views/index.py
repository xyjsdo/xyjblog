from flask import Blueprint, request

blue = Blueprint('first',__name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'

@blue.route('/blog/')
def blog():
    return 'blog'

@blue.route('/testrequest/')
def test_request():
    print(request.method)
    return 'success'

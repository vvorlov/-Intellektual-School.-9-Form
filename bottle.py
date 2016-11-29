# for run
import os

# bottle stuff
from bottle import run, request, get, post


# GET request handler
@get("/")
def hello():
    if 'name' not in request.query:
        return "Hello, World"

    name = request.query['name']
    return "Hello, %s" % name


# POST request handler
@post("/")
def post_hello():
    if 'name' not in request.query:
        return "Hello from POST, World"

    name = request.query['name']
    return "Hello from POST, %s" % name


# run
run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

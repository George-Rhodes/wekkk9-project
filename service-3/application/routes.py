from flask import Response, request, Flask
from application import app
import requests
import random, string



@app.route('/number', methods=['GET'])
def number():
    number = str(random.randint(0,9)) + str(random.randint(0,9))
    return Response(number, mimetype='text/plain')
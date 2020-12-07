from flask import redirect, url_for, Response, request
from application import app
import requests
import random




@app.route('/alpha', methods=['GET'])
def alpha():
    alpha_List=["A","B","C","D","E","F","G","G","G","H","K","K","K","K","K","K","K"]
    alpha1 = random.choice(alpha_List)
    alpha2 = random.choice(alpha_List)
    alphas = alpha1 + alpha2
    return Response(alphas, mimetype='text/plain')
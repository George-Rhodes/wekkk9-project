from application import app
from flask import Response, request
import random


@app.route('/prize', methods=['POST'])
def prize():
    response=request.data.decode('utf-8')
    if response[0] == "K" and response[1] == "K" :
        prize = "Death"
    elif response[0] == "K" or response[1] == "K" :
        prize = "lose a limb"
    elif response[0] == "G" and response[1] == "G" :
        prize = "you have won a life time supply of money , trip to the Bahamas, and your own private island. Our agent will contact you shortly, dont worry we know where you live"
    elif response[0] == "G" or response[1] == "G" :
        prize = "You have won a tenner"
    else:
        prize = "sorry, you win nothing"
    return Response(prize, mimetype='text/plain')
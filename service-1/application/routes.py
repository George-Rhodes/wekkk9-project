from flask import redirect, url_for, Response, request, render_template
from application import app, db
from application.models import ticket_prize
import requests
import random

@app.route('/')

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html', title='click the lotto button')

@app.route('/lotto', methods=['GET', 'POST'])
def lotto():
    alpha=requests.get('http://service-2:5001/alpha')
    number=requests.get('http://service-3:5002/number')
    ticket= str(alpha.text) + str(number.text)
    prize=requests.post('http://service-4:5003/prize', data=ticket)
    prize_str = str(prize.text)
    ted= ticket_prize(ticket_num=ticket, prize_info=prize_str)
    db.session.add(ted)
    db.session.commit()
    return render_template('lotto.html', title='lotto draw is', ticket=ticket, prize=prize.text)
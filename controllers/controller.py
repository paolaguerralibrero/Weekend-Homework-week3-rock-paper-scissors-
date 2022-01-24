from flask import render_template
from flask import Flask
from app import app
from models.game import Game


@app.route('/rules')
def rules():
    return render_template('rules.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<choice_1>/<choice_2>')
def index(choice_1, choice_2):
    game = Game(choice_1, choice_2)
    result = game.check_win()
    return render_template('index.html', result=result)

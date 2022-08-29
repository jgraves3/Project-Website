from app import app
from flask import render_template
from app.forms import TakerInfoForm 
@app.route('/')
@app.route('/questions')
def index():
    form = TakerInfoForm()
    return render_template('prequestions.html', form = form)

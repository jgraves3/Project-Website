from app import app
from flask import render_template, redirect
from app.forms import TakerInfoForm 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TakerInfoForm()
    return render_template('prequestions.html', form = form)

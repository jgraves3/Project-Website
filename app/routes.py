from app import app
from flask import render_template, redirect
from app.forms import TakerInfoForm, FacebookForm, GoogleForm, MicrosoftForm, TwitterForm, AmazonForm

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/prequestions')

@app.route('/prequestions', methods=['GET', 'POST'])
def prequestions():
    form = TakerInfoForm()
    if form.validate_on_submit():
        return redirect('/facebook')
    return render_template('prequestions.html', form = form)

@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    form = FacebookForm()
    if form.validate_on_submit():
        return redirect('/google')
    return render_template('facebook.html', form = form)


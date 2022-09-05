from app.ask import bp
from flask import render_template, redirect, url_for
from app.ask.forms import TakerInfoForm, FacebookForm, GoogleForm, MicrosoftForm, TwitterForm, AmazonForm

@bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('ask.prequestions'))

@bp.route('/prequestions', methods=['GET', 'POST'])
def prequestions():
    form = TakerInfoForm()
    if form.validate_on_submit():
        return redirect(url_for('ask.facebook'))
    return render_template('ask/prequestions.html', form = form)

@bp.route('/facebook', methods=['GET', 'POST'])
def facebook():
    form = FacebookForm()
    if form.validate_on_submit():
        return redirect('/google')
    return render_template('ask/facebook.html', form = form)


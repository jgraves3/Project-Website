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
        if form.useFacebook.data == True:
            return redirect(url_for('ask.facebook'))
        elif form.useGoogle.data == True:
            return redirect(url_for('ask.google'))
        elif form.useMicrosoft.data == True:
            return redirect(url_for('ask.microsoft'))
        elif form.useTwitter.data == True:
            return redirect(url_for('ask.twitter'))
        elif form.useAmazon.data == True:
            return redirect(url_for('ask.amazon'))
        else:
            return redirect(url_for('ask.thanks'))
    return render_template('ask/prequestions.html', form = form)

@bp.route('/facebook', methods=['GET', 'POST'])
def facebook():
    form = FacebookForm()
    if form.validate_on_submit():
        return redirect('/google')
    return render_template('ask/facebook.html', form = form)

@bp.route('/google', methods=['GET', 'POST'])
def google():
    form = GoogleForm()
    if form.validate_on_submit():
        return redirect('/microsoft')
    return render_template('ask/google.html', form = form)

@bp.route('/microsoft', methods=['GET', 'POST'])
def microsoft():
    form = MicrosoftForm()
    if form.validate_on_submit():
        return redirect('/twitter')
    return render_template('ask/microsoft.html', form = form)

@bp.route('/twitter', methods=['GET', 'POST'])
def twitter():
    form = TwitterForm()
    if form.validate_on_submit():
        return redirect('/amazon')
    return render_template('ask/twitter.html', form = form)

@bp.route('/amazon', methods=['GET', 'POST'])
def amazon():
    form = AmazonForm()
    if form.validate_on_submit():
        return redirect('/thanks')
    return render_template('ask/amazon.html', form = form)

@bp.route('/thanks', methods=['GET', 'POST'])
def thanks():
   return render_template('ask/thanks.html') 

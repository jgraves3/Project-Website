from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange

class TakerInfoForm(FlaskForm):
    age = IntegerField(label='Age: ', validators = [Optional(), NumberRange(18, 100)])
    #Change to a radio field
    gender = SelectField(label = 'Gender: ', choices=['Male', 'Female', 'Non-Binary'], validators=[Optional()])
    education = SelectField(label='Highest level of education you have achieved: ', choices=[('high school', 'High School/GED'),
                                                                                            ('some college', 'Some College'),
                                                                                            ('bachelors', 'Bachelor\'s'),
                                                                                            ('grad school', 'Graduate School')],
                                                                                            validators = [Optional()]
                                                                                            )
    major = StringField(label="Major: ", validators = [Optional()])
    timeSpent = SelectField(label='How much time do you spend on average using a computer or mobile device daily?',
                            choices = [(1, '1 hour or less'), 
                                       (2, '2 hours or less'),
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'),
                                       (5, '5 hours or less'), 
                                       (6, '6 hours or less'),
                                       (7, '7 or more hours')],
                            validators = [DataRequired()])
    submit = SubmitField('Next Page')

class FacebookForm(FlaskForm):
    usage = BooleanField(label='Do you use Facebook or Instagram?', validators=[DataRequired()])
    timeSpent = SelectField(label='How much time do you spend on average using Facebook (or Instagram)?', 
                            choices = [(1, '1 hour or less'),
                                       (2, '2 hours or less'), 
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'), 
                                       (5, '5 hours or more')
                                       ],
                            validators = [DataRequired()])

class GoogleForm(FlaskForm):
    usage = BooleanField(label='Do you use Google (Google Search, Google Maps, Google Images, etc.)?', validators = [DataRequired()])

class MicrosoftForm(FlaskForm):
    usage = BooleanField(label='Do you use Microsoft\'s services (Windows, Xbox Live, etc.)?', validators = [DataRequired()])

class TwitterForm(FlaskForm):
    usage = BooleanField(label='Do you use Twitter?', validators = [DataRequired()])
class AmazonForm(FlaskForm):
    usage = BooleanField(label='Do you use Amazon?', validators = [DataRequired()])

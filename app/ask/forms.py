from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, SubmitField, BooleanField, TextAreaField
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
    purpose = TextAreaField(label='What is (in your opinion) the purpose of Facebook?')
    harm = RadioField(label = 'Facebook is harmful to the general public.',
                       choices=[(1, 'Strongly Disagree'),
                                (2, 'Disagree'),
                                (3, 'Neutral'),
                                (4, 'Agree'),
                                (5, 'Strongly Agree')
                                ]
                       )
    whyHarm = TextAreaField(label='Please explain your response to the previous question.')
    service = RadioField(label = 'Facebook acts in service to the public good.', 
                         choices = [(1, 'Strongly Disagree'),
                                    (2, 'Disagree'), 
                                    (3, 'Neutral'), 
                                    (4, 'Agree'),
                                    (5, 'Strongly Agree')
                                    ]
                         )
    whyService = TextAreaField(label='Please explain your response to the previous question.')
    privacy = RadioField(label='Facebook respects the privacy of its users.', 
                            choices = [(1, 'Strongly Disagree'),
                                       (2, 'Disagree'),
                                       (3, 'Neutral'),
                                       (4, 'Agree'),
                                       (5, 'Strongly Agree')
                                       ]
                            )
    whyPrivacy = TextAreaField('Please explain your response to the previous question.')
    submit = SubmitField('Next Page')
class GoogleForm(FlaskForm):
    usage = BooleanField(label='Do you use Google (Google Search, Google Maps, Google Images, etc.)?', validators = [DataRequired()])
class MicrosoftForm(FlaskForm):
    usage = BooleanField(label='Do you use Microsoft\'s services (Windows, Microsoft Teams, etc.)?', validators = [DataRequired()])

class TwitterForm(FlaskForm):
    usage = BooleanField(label='Do you use Twitter?', validators = [DataRequired()])
class AmazonForm(FlaskForm):
    usage = BooleanField(label='Do you use Amazon?', validators = [DataRequired()])

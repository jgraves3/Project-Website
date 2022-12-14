from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange

class TakerInfoForm(FlaskForm):
    age = IntegerField(label='Age: ', validators = [Optional(), NumberRange(18, 100)])
    #Change to a radio field?
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
                            )
    # ADD THE 'Do you use ...' QUESTIONS HERE FOR EASIER DEV WORK
    useFacebook = BooleanField(label='Do you use Facebook or Facebook services?', 
                             # choices = [(True, 'Yes'),
                             #            (False, 'No')
                             #            ],
                              )
    useGoogle = BooleanField(label='Do you use Google services?', 
                             #choices = [(True, 'Yes'),
                             #          (False, 'No')
                             #          ],
                            )
    useMicrosoft = BooleanField(label='Do you use Microsoft services?',
                              # choices = [(True, 'Yes'), 
                               #           (False, 'No')
                               #           ],
                            )
    useTwitter = BooleanField(label='Do you use Twitter?', 
                            #choices = [(True, 'Yes'),
                             #          (False, 'No')
                              #         ],
                             )
    useAmazon = BooleanField(label='Do you use Amazon services?', 
                           # choices = [(True, 'Yes'), 
                            #           (False, 'No')
                             #          ],
                            )
    submit = SubmitField('Next Page')

class FacebookForm(FlaskForm):
   # usage = BooleanField(label='Do you use Facebook or Instagram?', validators=[DataRequired()])
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
    #usage = BooleanField(label='Do you use Google (Google Search, Google Maps, Google Images, etc.)?', validators = [DataRequired()])
    timeSpent = SelectField(label='How much time do you spend on average using Google (Google Search, Google Maps, Google Images, etc.)?', 
                            choices = [(1, '1 hour or less'),
                                       (2, '2 hours or less'), 
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'), 
                                       (5, '5 hours or more')
                                       ],
                            validators = [DataRequired()])
    purpose = TextAreaField(label='What is (in your opinion) the purpose of Google?')
    harm = RadioField(label = 'Google is harmful to the general public.',
                       choices=[(1, 'Strongly Disagree'),
                                (2, 'Disagree'),
                                (3, 'Neutral'),
                                (4, 'Agree'),
                                (5, 'Strongly Agree')
                                ]
                       )
    whyHarm = TextAreaField(label='Please explain your response to the previous question.')
    service = RadioField(label = 'Google acts in service to the public good.', 
                         choices = [(1, 'Strongly Disagree'),
                                    (2, 'Disagree'), 
                                    (3, 'Neutral'), 
                                    (4, 'Agree'),
                                    (5, 'Strongly Agree')
                                    ]
                         )
    whyService = TextAreaField(label='Please explain your response to the previous question.')
    privacy = RadioField(label='Google respects the privacy of its users.', 
                            choices = [(1, 'Strongly Disagree'),
                                       (2, 'Disagree'),
                                       (3, 'Neutral'),
                                       (4, 'Agree'),
                                       (5, 'Strongly Agree')
                                       ]
                            )
    whyPrivacy = TextAreaField('Please explain your response to the previous question.')
    submit = SubmitField('Next Page')
class MicrosoftForm(FlaskForm):
    #usage = BooleanField(label='Do you use Microsoft\'s services (Windows, Microsoft Teams, etc.)?', validators = [DataRequired()])
    timeSpent = SelectField(label='How much time do you spend on average using Microsoft\'s services (Windows, Teams, etc.)?', 
                            choices = [(1, '1 hour or less'),
                                       (2, '2 hours or less'), 
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'), 
                                       (5, '5 hours or more')
                                       ],
                            validators = [DataRequired()])
    purpose = TextAreaField(label='What is (in your opinion) the purpose of Microsoft?')
    harm = RadioField(label = 'Microsoft is harmful to the general public.',
                       choices=[(1, 'Strongly Disagree'),
                                (2, 'Disagree'),
                                (3, 'Neutral'),
                                (4, 'Agree'),
                                (5, 'Strongly Agree')
                                ]
                       )
    whyHarm = TextAreaField(label='Please explain your response to the previous question.')
    service = RadioField(label = 'Microsoft acts in service to the public good.', 
                         choices = [(1, 'Strongly Disagree'),
                                    (2, 'Disagree'), 
                                    (3, 'Neutral'), 
                                    (4, 'Agree'),
                                    (5, 'Strongly Agree')
                                    ]
                         )
    whyService = TextAreaField(label='Please explain your response to the previous question.')
    privacy = RadioField(label='Microsoft respects the privacy of its users.', 
                            choices = [(1, 'Strongly Disagree'),
                                       (2, 'Disagree'),
                                       (3, 'Neutral'),
                                       (4, 'Agree'),
                                       (5, 'Strongly Agree')
                                       ]
                            )
    whyPrivacy = TextAreaField('Please explain your response to the previous question.')
    submit = SubmitField('Next Page')
class TwitterForm(FlaskForm):
    #usage = BooleanField(label='Do you use Twitter?', validators = [DataRequired()])
    timeSpent = SelectField(label='How much time do you spend on average using Twitter?', 
                            choices = [(1, '1 hour or less'),
                                       (2, '2 hours or less'), 
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'), 
                                       (5, '5 hours or more')
                                       ],
                            validators = [DataRequired()])
    purpose = TextAreaField(label='What is (in your opinion) the purpose of Twitter?')
    harm = RadioField(label = 'Twitter is harmful to the general public.',
                       choices=[(1, 'Strongly Disagree'),
                                (2, 'Disagree'),
                                (3, 'Neutral'),
                                (4, 'Agree'),
                                (5, 'Strongly Agree')
                                ]
                       )
    whyHarm = TextAreaField(label='Please explain your response to the previous question.')
    service = RadioField(label = 'Twitter acts in service to the public good.', 
                         choices = [(1, 'Strongly Disagree'),
                                    (2, 'Disagree'), 
                                    (3, 'Neutral'), 
                                    (4, 'Agree'),
                                    (5, 'Strongly Agree')
                                    ]
                         )
    whyService = TextAreaField(label='Please explain your response to the previous question.')
    privacy = RadioField(label='Twitter respects the privacy of its users.', 
                            choices = [(1, 'Strongly Disagree'),
                                       (2, 'Disagree'),
                                       (3, 'Neutral'),
                                       (4, 'Agree'),
                                       (5, 'Strongly Agree')
                                       ]
                            )
    whyPrivacy = TextAreaField('Please explain your response to the previous question.')
    submit = SubmitField('Next Page')
class AmazonForm(FlaskForm):
    #usage = BooleanField(label='Do you use Amazon?', validators = [DataRequired()])
    timeSpent = SelectField(label='How much time do you spend on average using Amazon?', 
                            choices = [(1, '1 hour or less'),
                                       (2, '2 hours or less'), 
                                       (3, '3 hours or less'), 
                                       (4, '4 hours or less'), 
                                       (5, '5 hours or more')
                                       ],
                            validators = [DataRequired()])
    purpose = TextAreaField(label='What is (in your opinion) the purpose of Amazon?')
    harm = RadioField(label = 'Amazon is harmful to the general public.',
                       choices=[(1, 'Strongly Disagree'),
                                (2, 'Disagree'),
                                (3, 'Neutral'),
                                (4, 'Agree'),
                                (5, 'Strongly Agree')
                                ]
                       )
    whyHarm = TextAreaField(label='Please explain your response to the previous question.')
    service = RadioField(label = 'Amazon acts in service to the public good.', 
                         choices = [(1, 'Strongly Disagree'),
                                    (2, 'Disagree'), 
                                    (3, 'Neutral'), 
                                    (4, 'Agree'),
                                    (5, 'Strongly Agree')
                                    ]
                         )
    whyService = TextAreaField(label='Please explain your response to the previous question.')
    privacy = RadioField(label='Amazon respects the privacy of its users.', 
                            choices = [(1, 'Strongly Disagree'),
                                       (2, 'Disagree'),
                                       (3, 'Neutral'),
                                       (4, 'Agree'),
                                       (5, 'Strongly Agree')
                                       ]
                            )
    whyPrivacy = TextAreaField('Please explain your response to the previous question.')
    submit = SubmitField('Next Page')

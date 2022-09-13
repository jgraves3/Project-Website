from app import db

class Prequestions(db.Model):
    __tablename__ = 'prequestions'
    id = db.Column(db.Integer, primary_key=True) #Discren individual responses from one-another
    age = db.Column(db.Integer, index=True)
    gender = db.Column(db.String(15), index=True)
    education = db.Column(db.String(15), index=True)
    major = db.Column(db.String(15), index=True)
    timeSpent = db.Column(db.String(64), index=True)
    useFacebook = db.Column(db.Boolean, nullable = False)
    useGoogle = db.Column(db.Boolean, nullable = False)
    useMicrosoft = db.Column(db.Boolean, nullable = False)
    useTwitter = db.Column(db.Boolean, nullable = False)
    useAmazon = db.Column(db.Boolean, nullable = False)

    facebook = db.relationship("Facebook", backref = "prequestions", uselist = False)
    google = db.relationship("Google", backref = "prequestions", uselist = False)
    microsoft = db.relationship("Microsoft", backref = "prequestions", uselist = False)
    twitter = db.relationship("Twitter", backref = "prequestions", uselist = False)
    amazon = db.relationship("Amazon", backref = "prequestions", uselist = False)
    
    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(self.age, self.gender, self.education, self.major, self.timeSpent)

class Facebook(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, db.ForeignKey('prequestions.useFacebook'), nullable = False)
    purpose = db.Column(db.Text, nullable=True)
    harm = db.Column(db.Integer, nullable=True)
    whyHarm = db.Column(db.Text, nullable=True)
    service = db.Column(db.Integer, nullable=True)
class Google(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, db.ForeignKey('prequestions.useGoogle'), nullable=False)
class Microsoft(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, db.ForeignKey('prequestions.useMicrosoft'), nullable=False)
class Twitter(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, db.ForeignKey('prequestions.useTwitter'), nullable=False)
class Amazon(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, db.ForeignKey('prequestions.useAmazon'), nullable=False)

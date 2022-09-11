from app import db

class Prequestions(db.Model):
   id = db.Column(db.Integer, primary_key=True) #Discren individual responses from one-another
   age = db.Column(db.Integer, index=True)
   gender = db.Column(db.String(15), index=True)
   education = db.Column(db.String(15), index=True)
   major = db.Column(db.String(15), index=True)
   timeSpent = db.Column(db.String(64), index=True) 

   def __repr__(self):
       return '{}, {}, {}, {}, {}'.format(self.age, self.gender, self.education, self.major, self.timeSpent)

class Facebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usage = db.Column(db.Boolean, nullable=False)
    purpose = db.Column(db.Text, nullable=True)
    harm = db.Column(db.Integer, nullable=True)
    whyHarm = db.Column(db.Text, nullable=True)

class Google(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, nullable=False)
class Microsoft(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, nullable=False)
class Twitter(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, nullable=False)
class Amazon(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('prequestions.id'), primary_key=True)
    usage = db.Column(db.Boolean, nullable=False)

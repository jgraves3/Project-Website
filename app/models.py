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

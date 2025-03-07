from blueprintapp.app import db

class User(db.Model):
    __tablename__ = 'user'

    pid = db.Column( db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)
    job = db.Column(db.String)

    def __repr__(self):
        return f"Name: {self.name}, Job: {self.job}, Age: {self.age}"

    def get_id(self):
        return self.pid

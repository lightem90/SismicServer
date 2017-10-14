from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from Database.database import Base
from sqlalchemy import inspect


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    secret = Column(String(64), unique=False)
    address = Column(String(120), unique=False)
    phone = Column(String(15), unique=False)
    qualification = Column(String(120), unique=False)
    registration = Column(String(120), unique=False)
    registration_date = Column(DateTime, unique=False)
    confirmed = Column(Integer, unique=False)  # ?

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __init__(self, email, secret, name=None, address=None, phone=None, qualification=None, registration=None,
                 registrationdate=None):
        self.email = email
        self.secret = secret
        self.name = name
        self.address = address
        self.phone = phone
        self.qualification = qualification
        self.registration = registration
        if registrationdate is None:
            self.registrationDate = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.name

    def hash_password(self, password):
        # obj = AES.new(self.name, AES.MODE_CBC, self.email)
        # self.secret = obj.encrypt(password)
        return password

    def verify_password(self, password):
        # obj = AES.new(self.name, AES.MODE_CBC, self.email)
        # return password == obj.decrypt(self.secret)
        return True


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(120), ForeignKey("users.email"), nullable=False)
    # depends on how "pretty" the json is (14k is for a normal report in one line)
    data = Column(String(28000))

    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from Database.database import Base
from Crypto.Cipher import AES


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    secret = Column(String(128), unique=True)
    address = Column(String(120), unique=False)
    phone = Column(String(15), unique=False)
    qualification = Column(String(120), unique=False)
    registration = Column(String(120), unique=False)
    registration_date = Column(DateTime, unique=False)
    confirmed = Column(Integer, unique=False)

    def __init__(self, email, password, name=None, address=None, phone=None, qualification=None, registration=None,
                 registrationdate=None):
        self.email = email
        self.password = password
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
        obj = AES.new(self.name, AES.MODE_CBC, self.email)
        self.secret = obj.encrypt(password)

    def verify_password(self, password):
        obj = AES.new(self.name, AES.MODE_CBC, self.email)
        return password == obj.decrypt(self.secret)


class SismicLocation(Base):
    __tablename__ = 'InformazioniLocazioneSismica'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, unique=False)

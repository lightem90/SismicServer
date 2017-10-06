from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from Database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    address = Column(String(120), unique=False)
    phone = Column(String(12), unique=False)
    qualification = Column(String(120), unique=False)
    registration = Column(String(120), unique=False)
    registration_date = Column(DateTime, unique=False)
    confirmed = Column(Integer, unique=False)

    def __init__(self, name=None, email=None, address=None, phone=None, qualification=None, registration=None, registrationDate = None):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.qualification = qualification
        self.registration = registration
        if registrationDate is None:
            self.registrationDate = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.name


class SismicLocation(Base):
    __tablename__ = 'InformazioniLocazioneSismica'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, unique=False)


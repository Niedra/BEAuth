import cryptacular.bcrypt
import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    email = Column(Unicode(255), unique=True)

    _password = Column(Unicode(255))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        hashed = bcrypt.encode(value)
        self._password = hashed

    @classmethod
    def by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    def check_password(self, password):
        return bcrypt.check(self.password, password)

def populate():
    session = DBSession()
    user = User(name=u'admin', password=u'password',
                email=u'noreply@example.com')
    session.add(user)
    session.flush()
    transaction.commit()
    
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()

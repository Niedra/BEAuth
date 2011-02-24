import transaction

from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.declarative import declarative_base 

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()

def populate():
    from beauth.models.user import User
    session = DBSession()
    user = User(name=u'admin', password=u'password',
                email=u'noreply@example.com', activated=True,
                verify_code='')
    session.add(user)
    session.flush()
    transaction.commit()

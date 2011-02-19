def _initTestingDB():
    from sqlalchemy import create_engine
    from beauth.models import initialize_sql
    session = initialize_sql(create_engine('sqlite://'))
    return session

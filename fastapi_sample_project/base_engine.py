# region Required

####################################################
####################################################
from psycopg2cffi import compat

compat.register()
####################################################
####################################################
# endregion

# region Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# endregion

# region Engine

''' Oluşturduğumuz Veri tabanına bağlantı sağlamak.'''

engine = create_engine("postgresql://postgres:dD5Yz6xE5m@localhost:5435/dododeneme", pool_size=2000, max_overflow=0)
conn = engine.connect()
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
# endregion

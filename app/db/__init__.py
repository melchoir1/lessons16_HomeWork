import sqlalchemy as sa

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = sa.create_engine("sqlite:///project.db", pool_recycle=600)
Session = sessionmaker(engine)

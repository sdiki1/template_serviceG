from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    MetaData,
    DateTime,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "..."
password = "..."
host = "..."
db_name = "..."
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db_name}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class SMS(Base):
    __tablename__ = "sms"

    ...


class Accounts(Base):
    __tablename__ = "accounts_wb"
    ...


class modems(Base):
    __tablename__ = "modems"

    ...


class open_accs(Base):
    __tablename__ = "open_accounts_wb"

    ...


Base.metadata.create_all(engine)

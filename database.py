from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
POSTGRESQL_DATABASE_URL = "postgres://tfvlhcqm:FoeFars7s6HwT3XoxAvbJAXxkBw_uwH_@hattie.db.elephantsql.com/tfvlhcqm"
# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# MYSQL Series
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
engine = create_engine(
    POSTGRESQL_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

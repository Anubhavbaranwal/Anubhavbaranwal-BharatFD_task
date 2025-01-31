from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
 

sqlalchemy_database_url = "sqlite:///./blog.db" 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(sqlalchemy_database_url,connect_args={"check_same_thread":False}) 
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 
Base = declarative_base() 







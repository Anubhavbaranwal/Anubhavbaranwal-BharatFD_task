from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
 

sqlalchemy_database_url = "postgresql://neondb_owner:npg_on8O0jEreMLu@ep-black-water-a8jayev1-pooler.eastus2.azure.neon.tech/neondb?sslmode=require" 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(sqlalchemy_database_url) 
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 
Base = declarative_base() 


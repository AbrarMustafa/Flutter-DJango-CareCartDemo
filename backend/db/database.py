from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Settings

# print(str(settings.DATABASE_URL))
engine = create_engine(Settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

 # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


        
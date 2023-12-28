from sqlalchemy.orm import Session
from app.core.database import SessionLocal

# Dependency to get the database session
def get_db():
    db = SessionLocal() #db = Session(bind=engine)  # Pass the engine to the Session
    try:
        yield db
    finally:
        db.close()

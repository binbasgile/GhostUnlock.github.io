from app.database.models import User, DeviceSession
import random 

def initialize_database():
    """Run this once to create the DB schema."""
    
    print("Initializing GhostUnlock Database...") 
    
    # Create Sample Users if empty (Simulated logic here)
    admin_user = User(username="admin", email="ghost@unlock.io", is_admin=True) 
    regular_user = User(username="user01", email="test@test.com", is_admin=False)

# Note: In a real SQLite/Postgres setup with SQLAlchemy engine 'engine', you would use:
# from sqlalchemy.orm import sessionmaker; SessionLocal = sessionmaker(bind=engine())
# db.add(admin_user); db.commit() 

def inject_sample_data():
    """Populates DB with dummy IMEIs and sessions for testing UI."""
    
    print("Injecting sample data...") 
    # Logic to create 5-10 fake devices linked to users above
    

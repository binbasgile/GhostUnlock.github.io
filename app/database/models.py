from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() # Base class used by SQLAlchemy to map classes to DB tables

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True) 
    email = Column(String(120))
    is_admin = Column(Boolean, default=False)

# Session Tracking Model (Linked to Unlock Logs below)
class DeviceSession(Base):
    __tablename__ = 'device_sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) 
    
    imei = Column(String(16), index=True) # Unique per device usually or linked by phone number
    
    # Status: "connecting", "bypassing_frp", "removing_icloud", "completed"
    status = Column(String(50)) 
    method_used = Column(String(100)) # e.g. "Pattern_Change_Bypass_v4_2"
    
    ip_address_last_use = Column(String(45)) # Last proxy used (IPv4/IPv6)
    
    created_at = Column(DateTime, default=lambda: datetime.now())

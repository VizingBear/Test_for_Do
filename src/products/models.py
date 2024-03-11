from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, server_default='True')

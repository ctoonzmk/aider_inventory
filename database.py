from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/inventory_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, unique=True, index=True)
    quantity = Column(Integer)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    invoice_no = Column(String, unique=True, index=True)
    date = Column(DateTime)
    customer = Column(String)
    job = Column(String)
    salesperson = Column(String)
    contact = Column(String)
    phone = Column(String)
    sold_to = Column(String)
    ship_to = Column(String)
    customer_po = Column(String)
    ship_via = Column(String)
    fob = Column(String)
    terms = Column(String)

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)

# TODO: Add more models as needed

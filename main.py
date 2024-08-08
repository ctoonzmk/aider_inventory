from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
import models
import pdf_processor

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this with your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.post("/upload-order")
async def upload_order(file: UploadFile = File(...)):
    contents = await file.read()
    order_data = pdf_processor.process_order_pdf(contents)
    # TODO: Save order data to database and update inventory
    return {"message": "Order processed successfully", "data": order_data}

@app.post("/upload-return")
async def upload_return(file: UploadFile = File(...)):
    contents = await file.read()
    return_data = pdf_processor.process_return_pdf(contents)
    # TODO: Save return data to database and update inventory
    return {"message": "Return processed successfully", "data": return_data}

@app.get("/inventory")
async def get_inventory():
    # TODO: Fetch inventory data from database
    return {"message": "Inventory data fetched successfully", "data": []}

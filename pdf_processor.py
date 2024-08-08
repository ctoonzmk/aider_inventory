import fitz  # PyMuPDF

def process_order_pdf(pdf_content):
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    # TODO: Implement logic to extract required fields from the text
    # This is a placeholder implementation
    order_data = {
        "invoice_no": "Extract invoice number",
        "date": "Extract date",
        "customer": "Extract customer",
        "job": "Extract job",
        "salesperson": "Extract salesperson",
        "contact": "Extract contact",
        "phone": "Extract phone",
        "sold_to": "Extract sold to information",
        "ship_to": "Extract ship to information",
        "customer_po": "Extract customer PO",
        "ship_via": "Extract ship via",
        "fob": "Extract F.O.B.",
        "terms": "Extract terms",
    }
    
    return order_data

def process_return_pdf(pdf_content):
    # TODO: Implement similar logic as process_order_pdf
    # but for return PDFs
    return {}

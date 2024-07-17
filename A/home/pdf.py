from reportlab.pdfgen import canvas
from io import BytesIO


def create_pdf(name , number):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"{name}-{number}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer



    
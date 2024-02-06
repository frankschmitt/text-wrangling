import sys
from reportlab.pdfgen.canvas import Canvas
from datetime import datetime
# Creates a PDF file from scratch, containing some text

# read file name from first command-line argument
file_name = sys.argv[1]

canvas = Canvas(file_name, pagesize=(612, 792))
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
canvas.drawString(72, 72, "Hello, World! in " + file_name + " at " + timestamp)
canvas.save()

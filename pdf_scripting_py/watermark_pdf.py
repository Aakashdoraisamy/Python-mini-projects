from PyPDF2 import PdfReader, PdfWriter
import PyPDF2

template = PyPDF2.PdfReader(open("merged_output.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("watermark.pdf", "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0]) 
    output.add_page(page)

with open("watermarked_output.pdf", "wb") as file:
    output.write(file)

print("Watermark applied to all pages and saved as 'watermarked_output.pdf'")

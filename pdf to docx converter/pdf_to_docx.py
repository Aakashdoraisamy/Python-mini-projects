from pdf2docx import Converter

pdf_file = 'Aakash Resume.pdf'
docx_file = 'Aakash Resume.docx'

cv = Converter(pdf_file) 
cv.convert(docx_file, start=0, end=None) 
cv.close()

print('File converted Successfully......')
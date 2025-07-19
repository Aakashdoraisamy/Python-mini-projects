import PyPDF2
import sys

inputs = sys.argv[1:]

def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged_output.pdf")
    print("Merged PDFs into 'merged_output.pdf'")
    
merge_pdfs(inputs)
import PyPDF2
import os
import sys

def pdf_reader(pdf_file):


    pdf_file_obj = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    tot_pages = pdf_reader.getNumPages()
        
    title_page = pdf_reader.getPage(0)
    text = title_page.extractText()

    print("File: ", pdf_file)
    print("Contains ", tot_pages, " pages")
    print(text)

pdf_reader(sys.argv[1])

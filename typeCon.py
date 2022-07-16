from pdf2docx import Converter
from docx2pdf import convert
import cv2 as cv
from img2pdf import Image
import io
pdf_am="ICS unit.pdf"
docx_am="IcsOutput.docx"

def pdftoDoc(path):
    cv=Converter(path)
    cv.convert(docx_am,start=0,end=None)
    cv.close()
    print("convert done!")

def docxtoPdf(path):
    convert(path)
    

def pngToPdf(path):
    pdf=Image.open(path)
    pdf.save('output.pdf')
    return pdf
    #

def pngToJpg(path):
    img_png = Image.open(path)
    img_png.save('outputpngtojpg.jpg')
    return img_png


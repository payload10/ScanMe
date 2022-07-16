import numpy
from django.shortcuts import render,HttpResponse
import documentScanner as ds
import cv2 as cv
import scan_me as sm
import typeCon as tc
from .models import File
from PIL import Image
# Create your views here

def home(request):
    n=1
    if request.method=='GET':
        return render (request,"index1.html")
    if request.method=="POST":
        fname=request.FILES['image'].read()
        npimg=numpy.fromstring(fname,numpy.uint8)
        img=cv.imdecode(npimg,cv.IMREAD_UNCHANGED)
        height,width= img.shape[:2]
        if height==width:
            height=width=500
        if width>height:
            width=550
            height=400
        if height>width:
            height=400
            width=300
        height=str(height)+'px'
        width=str(width)+'px'
        cv.imwrite("0.jpg",img)

        blurred_threshold = ds.transformation(img)
        cleaned_image = ds.final_image(blurred_threshold)
        context ={'height' : height,'width':width,'number':n}
        print(type(img))
        # cv.imwrite('image.jpg',image)
        return render(request,'next.html',context)

def display(request):
    if request.method=="POST":
        height=request.POST['height']
        width=request.POST['width']
        number=request.POST['number']
        number=int(number)+1
        if number > 5:
            sm.convert('5.jpg')
        context={'height' : height+'px','width':width+'px','number':number}
        print(height,width)
        return render(request,'next.html',context)

def forContrib(request):
    if request.method=="GET":
        return render(request,'activeContributors.html')

def fortheProject(request):
    if request.method=="GET":
        return render(request,'theProject.html')

def convert(request):
    if request.method=="POST":
        fname=request.FILES['image2'].read()
        npimg=numpy.fromstring(fname,numpy.uint8)
        img=cv.imdecode(npimg,cv.IMREAD_UNCHANGED)
        print(img)
        cv.imwrite("convert.jpg",img)
        return render(request,'convert.html')
    return render(request,'convert.html')

def convertPng(request):
    if request.method=="POST":
        fname=request.FILES['image2'].read()
        npimg=numpy.fromstring(fname,numpy.uint8)
        img=cv.imdecode(npimg,cv.IMREAD_UNCHANGED)
        print(img)
        cv.imwrite("pngimg.png",img)
        print("written")
        return render(request,'convert.html')
    return render(request,'convert.html')

def imgTopdf(request):
    pdf={'pdf':tc.pngToPdf("convert.jpg")}
    return render(request,'convert.html',pdf)


def pngToJpg(request):
    jpg={'jpg':tc.pngToJpg("pngimg.png")}
    return render(request,'convert.html',jpg)
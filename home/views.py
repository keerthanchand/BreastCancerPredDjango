from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
import os, shutil
import random
from .config import getfile


# Create your views here.

def index(request):
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid():
        	folder = './media/images'
        	for filename in os.listdir(folder):
        		file_path = os.path.join(folder, filename)
        		try:
        			if os.path.isfile(file_path) or os.path.islink(file_path):
        				os.unlink(file_path)
        			elif os.path.isdir(file_path):
        				shutil.rmtree(file_path)
        		except Exception as e:
        			print('Failed to delete %s. Reason: %s' % (file_path, e)) 

        	#newfile = request.POST.get('image').url
        	#print(newfile)
        	form.save()
        	image_file = os.listdir(folder)[0].split('.')[0]
        	
        	print(image_file)
        	

        	return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'index.html', {'form' : form}) 
  
  
def success(request):
	folder = './media/images'
	image_file = os.listdir(folder)[0].split('.')[0]
	result = getfile(image_file)
	context = {'result': result}
	return render(request, 'result.html', context) 

def display_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Images = imageUpload.objects.all()

        return render(request, 'display_image.html', 
                     {'model_images' : Images}) 



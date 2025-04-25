from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import UserDetail
#from .forms import UserDetailForm
import base64
import os
import json
import cv2
from PIL import Image
from io import BytesIO
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserDetail
import base64
from django.core.files.base import ContentFile
from django.contrib.auth import logout
import datetime

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(reverse('admin:index'))
            else:
                return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials.'})
    return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def user_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        photo_data = request.POST.get('photo')

        # Decode the photo data and save it
        format, imgstr = photo_data.split(';base64,')
        ext = format.split('/')[-1]
        photo = ContentFile(base64.b64decode(imgstr), name=f'{name}_{mobile}.{ext}')

        user_detail = UserDetail(name=name, age=age, sex=sex, mobile=mobile, address=address, photo=photo)
        user_detail.save()

        #return JsonResponse({'status': 'success', 'message': 'Form submitted successfully!'})
    
    return render(request, 'capture/user_form.html', {'message': 'Details submitted successfully!'})

def save_photo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image']
        image_data = image_data.split(',')[1]
        image_data = base64.b64decode(image_data)

        # Save the image temporarily
        image = Image.open(BytesIO(image_data))
        cap_img = "captured_photo_" + str(datetime.datetime.now().timestamp())+".png"
        global image_path 
        image_path = os.path.join(settings.MEDIA_ROOT, "photos/"+cap_img)
        image.save(image_path)

        # Convert the image to OpenCV format 
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 

        # Detect faces 
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) != 1:
            return JsonResponse({'quality': 0, 'message': 'Ensure there is exactly one face in the frame.'})

        # Assess the image quality (a simple brightness check as a placeholder)
        quality = assess_image_quality(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))

        return JsonResponse({'quality': quality})
    return JsonResponse({'quality': 0})

def assess_image_quality(image):
    # Placeholder for a real quality assessment algorithm
    gray_image = image.convert('L')
    histogram = gray_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for i in range(len(histogram)):
        ratio = histogram[i] / pixels
        brightness += ratio * (-scale + i)

    quality = (brightness / scale) * 100
    return round(quality)

def user_form(request):
    return render(request, 'form.html')

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        #photo = request.POST.get('photo')
        
        # Save the user details
        UserDetail.objects.create(
            name=name,
            age=age,
            sex=sex,
            mobile=mobile,
            address=address,
            photo=image_path,
        )
        
        return redirect('index')
    
def logout_view(request):
    logout(request)
    return redirect('login')

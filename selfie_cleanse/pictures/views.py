from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from pictures.selfie_recognition import SelfieDetection
import base64
import io
# Create your views here.

selfie_detection = SelfieDetection()

def upload_file(request):
    if request.method == 'POST':
        print(request)
        image = request.form['img']
        if selfie_detection.is_selfie(io.BytesIO(base64.b64decode(image))):
            return HttpResponse("Is a selfie")
        else:
            return HttpResponse("Is not a selfie")

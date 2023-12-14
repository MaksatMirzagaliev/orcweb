from django.shortcuts import render
from django.http import HttpResponse
from .utils import text_recognition


def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        result = text_recognition(image)
        return render(request, 'ocrapp/result.html', {'result': result})
    return render(request, 'ocrapp/upload.html')

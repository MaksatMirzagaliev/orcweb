from django.shortcuts import render
from django.http import HttpResponse
from .utils import text_recognition


def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Получите данные изображения в виде байтов
        image = request.FILES['image'].read()

        # Передайте изображение в функцию text_recognition
        result = text_recognition(image)

        return render(request, 'ocrapp/result.html', {'result': result})

    return render(request, 'ocrapp/upload.html')

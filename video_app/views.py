from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'video_app/index.html')
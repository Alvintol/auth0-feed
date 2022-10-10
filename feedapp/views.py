from django.shortcuts import render

def index(request):
  return render(request, 'feedapp/index.html')


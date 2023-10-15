from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return render(request, "pages/index.html")

def search(request):
    input  = request.GET.get("input") or ""
    # input is the inputed text by the user

    # return list of products best fit
    return JsonResponse([product['post'] for post in products[start:end]], safe=False) 

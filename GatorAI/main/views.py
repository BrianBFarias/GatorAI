from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import spacy, re
from .models import Phone, Network

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def index(request):
    return render(request, "pages/index.html")

# check if we're looking for a network or mobile service
def NorM(doc):

    for token in doc:
        if token.text.lower() in ["network", "Wifi", "cable", "data"]:
            return False

        if token.text.lower() in ["iphone", "samsung", "google", "phone", "telephone", "mobile device"]:
            return True

    return False


def findPrice(text):
    pattern = r'(?:\$|price|cost|costs)\s*([\d.]+)'

    # Find the first match in the processed text
    match = re.search(pattern, text, flags=re.IGNORECASE)

    if match:
        # Convert the matched string to a float
        price = int(match.group(1))
        return price
    else:
        return None
    
def findStorage(text):
    pattern = r'(\d+)\s* ?[Gg][Bb]'

    # Find the first match in the sentence
    match = re.search(pattern, text, flags=re.IGNORECASE)

    if match:
        # Extract the matched number
        storage_capacity = int(match.group(1))
        return storage_capacity
    
    else:
        return None



def SpecPhone(doc, input):
    brand = None
    storage = None
    price = None
    cameras = None
    
    for token in doc:
        if token.text.lower() in ["Apple", "iPhone", "cable", "data"]:
            brand = token.text.capitalize()

        if token.text.lower() in ["google"]:
            brand = token.text.capitalize()

        if token.text.lower() in ["samsung"]:
            brand = token.text.capitalize()

        price = findPrice(input)
        storage = findStorage(input)

def SpecPlan(doc):
    pass

def search(request):
    input  = request.GET.get("input") or ""
    doc = nlp(input)
    # input is the inputed text by the user

    # we lookin for mobile or network service
    mobile = NorM(doc)

    if(mobile):
        SpecPhone(doc, input)
    elif(not mobile):
        SpecPlan(doc)

    # return list of products best fit
    # return JsonResponse([product['post'] for post in products[start:end]], safe=False) 
    return JsonResponse(False, safe=False) 


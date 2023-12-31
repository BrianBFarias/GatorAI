from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from itertools import chain
from django.http import JsonResponse
import spacy, re
from .models import Phone, Network

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def index(request):
    phones = Phone.objects.all()
    networks = Network.objects.all()

# Combine the querysets
    return render(request, "pages/index.html",{
        'phones': phones,
        'networks':networks,
    })

# check if we're looking for a network or mobile service
def NorM(doc):
    device = True

    for token in doc:
        if token.text.lower() in ["network", "wifi", "cable", "data", "plan"]:
            device = False

        if token.text.lower() in ["iphone", "samsung", "google", "phone", "telephone", "device", "phones"]:
            device = True

        if token.text.lower() in ["network", "Wifi", "cable", "data", "plan", "cellular", "data", "lines"]:
            return False

    return device

# find price of item if not found return none
def findPrice(text):
    pattern2 = r'\$(\d+(\.\d{2})?)'

    # Find the first match in the processed text
    match = re.search(pattern2, text)

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

def findCamera(text):
    pattern = r'(\d+)\s+(camera|lens)'

    # Use re.search to find the first match in the text
    match = re.search(pattern, text)

    # If a match is found, extract the number
    if match:
        return int(match.group(1))

    return None

def findLines(text):
    match = re.search(r'\b(\d+)\b\s*(line|people|person|family)\b', text)
    if match:
        print(int(match.group(1)))
        return int(match.group(1))
    else:
        return None
    
def findData(text):
    match = re.search(r'(\d+)\s*(?:GB|gb)\s*(?:of|plan)?\s*(?:data)?', text)
    if match:
        return int(match.group(1))
    else:
        return None

def SpecPhone(doc, input):
    brand = None
    
    for token in doc:
        if token.text.lower() in ["apple", "iPhone"]:
            brand = 'apple'

        if token.text.lower() in ["google"]:
            brand = token.text.capitalize()

        if token.text.lower() in ["samsung"]:
            brand = token.text.capitalize()

    price = findPrice(input)
    storage = findStorage(input)
    cameras = findCamera(input)

    products = Phone.objects.all()

    #filter based off whats not none
    if brand is not None:
        products = products.filter(type__icontains =brand)

    if storage is not None:
        products = products.filter(storage__gte = storage)

    if price is not None:
        products = products.filter(price__lte = price)

    if cameras is not None:
        products = products.filter(cameras__gte=cameras)

    return products

def SpecPlan(doc, input):
    section = "both"
    
    for token in doc:
        if token.text.lower() in ["wifi", "home", "internet","router"]:
            section = "home"
        if token.text.lower() in ["phone", "mobile", "device","telephone", "cellular", "cell"]:
            section = "mobile"

    rate = findPrice(input)
    lines = findLines(input)
    data = findData(input)

    products = Network.objects.all()

    #filter based off whats not none
    if section != "both":
        products = products.filter(type__icontains = section)

    if lines is not None:
        products = products.filter(lines__gte = lines)

    if data is not None:
        products = products.filter(data__gte = data)

    if rate is not None:
        products = products.filter(rate__lte = rate)

    return products

# main searching
def search(request):
    input  = request.GET.get("input") or ""
    doc = nlp(input)
    # input is the inputed text by the user
    print(input)
    # we lookin for mobile or network service
    mobile = NorM(doc)

    if(mobile):
        result= SpecPhone(doc, input)
    else:
        result = SpecPlan(doc, input)

    # for item in result:
    #     print(item)

    if not result:
        return JsonResponse(False, safe=False)
 
    # return list of products best fit like shown below as ex
    return JsonResponse([product.serialize() for product in result], safe=False) 
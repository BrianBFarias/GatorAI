from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .search import get_most_relevant


def index(request):
    return render(request, "pages/index.html")

def search(request, query):
    #can also pass in top_n argument for how many results to show
    relevant_entries = get_most_relevant(str(query))

#have to loop through entries to prepare data for template
    objects_data = []
    for entry in relevant_entries:
        object_data = {}
        #meta handles models with different structures
        for field in entry._meta.fields:
            object_data[field.verbose_name] = getattr(entry, field.name)
        objects_data.append(object_data)

#context gives template all the relevant data
    context = {'results': objects_data, "query": query}

    return render(request, 'pages/search.html', context)



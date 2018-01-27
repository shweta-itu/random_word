from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
    
    context = {
    "unique_id" : get_random_string(length=14)
    }

    
    if "counter" in request.session:
        request.session['counter'] += 1
    else:
        request.session["counter"] = 1
    print request.session["counter"]

    
    return render(request,'random_word_generator_app/index.html', context)


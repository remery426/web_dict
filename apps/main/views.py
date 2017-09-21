from django.shortcuts import render, redirect
from .word_search import translate


def index(request):

    return render(request,"main/index.html")
def search(request):
    response = translate(request.POST)
    if response['status'] == True:
        request.session['definition'] = response['definition'][0]
        request.session['word'] = response['word']
        return redirect('/')
    else:
        request.session["suggestions"] = response["suggestions"]
        return redirect("/suggest")
def suggest(request):
        context = {
            "suggestions": request.session["suggestions"]
        }
        return render(request,"main/suggest.html",context)

from .views.article_view import all_articles
from .views.article_view import test_response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# views.py

from django.shortcuts import render, redirect
from .forms import TwojFormularz

def moj_widok(request):
    if request.method == 'POST':
        form = TwojFormularz(request.POST)
        if form.is_valid():
            form.save()  # Zapisuje dane w bazie danych
            return redirect('sukces')  # Przekierowuje na stronę sukcesu
    else:
        form = TwojFormularz()

    return render(request, 'twoj_szablon.html', {'form': form})

def testORM ():
    query = None
    return HttpResponse(query)
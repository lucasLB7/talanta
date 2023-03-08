from django.shortcuts import render
from django.views.generic import TemplateView
def home(request):
    return render(request, 'main.html', {})
    #return render(request, 'header_footer.html', {})
    #return render(request, 'part.html', {})

# Create your views here.

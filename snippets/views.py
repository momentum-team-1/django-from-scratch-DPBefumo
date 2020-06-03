from django.shortcuts import render
from .models import Snippet

# Create your views here.
def home_page(request):
    snippets = Snippet.objects.all()
    return render(request, "snippets/home_page.html", {'snippets': snippets})
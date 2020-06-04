from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from users.models import User
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, "snippets/home_page.html")

@login_required
def list_snippet(request):
    snippets = request.user.snippets.all()
    return render(request, "snippets/list_snippet.html", {'snippets': snippets})

@login_required
def show_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)
    return render(request, "snippets/show_snippet.html", {"snippet": snippet})
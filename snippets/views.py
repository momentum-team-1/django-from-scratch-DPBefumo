from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Tag, search_snippets_for_user
from users.models import User
from django.contrib.auth.decorators import login_required
from .forms import SnippetForm



def home_page(request):
    if request.user.is_authenticated:
        return redirect(to='list_snippet')

    return render(request, "snippets/home_page.html")

def login(request):
    return render(request, "snippets/login.html")


@login_required
def profile_page(request):
    return render(request, "snippets/profile_page.html")


@login_required
def list_snippet(request):
    snippets = request.user.snippets.all()
    return render(request, "snippets/list_snippet.html", {'snippets': snippets})


@login_required
def snippet_detail(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)
    return render(request, "snippets/snippet_detail.html", {'snippet': snippet})


@login_required
def add_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)
    else:
        form = SnippetForm()
    
    return render(request, 'snippets/add_snippet.html', {'form': form})


@login_required
def edit_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)
    
    if request.method == "POST":
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)

    else:
        form = SnippetForm(instance=snippet, initial={"tag_names": snippet.get_tag_names()})
    
    return render(request, "snippets/edit_snippet.html", {'form': form, 'snippet': snippet})


@login_required
def delete_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)

    if request.method == 'POST':
        snippet.delete()
        return redirect(to='list_snippet')

    return render(request, "snippets/delete_snippet.html", {'snippet': snippet})


@login_required
def show_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    snippets = tag.snippets.filter(user=request.user)
    return render(request, "snippets/tag_detail.html", {"tag": tag, 'snippets': snippets})


@login_required
def search_snippets(request):
    query = request.GET.get('q')

    if query is not None:
        snippets = search_snippets_for_user(request.user, query)
    else:
        snippets = None
    
    return render(request, "snippets/search.html", {"snippets":snippets, "query":query})
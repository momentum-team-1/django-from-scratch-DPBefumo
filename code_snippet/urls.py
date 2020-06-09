"""code_snippet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from snippets import views as snippets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', snippets_views.home_page, name='home_page'),
    path('snippets/', snippets_views.list_snippet, name='list_snippet'),
    path('snippets/add/', snippets_views.add_snippet, name='add_snippet'),    
    path('snippets/<int:snippet_pk>/', snippets_views.snippet_detail, name='snippet_detail'),
    path('snippets/<int:snippet_pk>/edit/', snippets_views.edit_snippet, name='edit_snippet'),
    path('snippets/<int:snippet_pk>/delete/', snippets_views.delete_snippet, name='delete_snippet'),
    path('accounts/profile/', snippets_views.profile_page, name='profile_page')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

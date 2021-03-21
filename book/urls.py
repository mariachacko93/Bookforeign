"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from .views import bookCreateView,bookDeleteView,bookDetailView,bookListView,bookUpdateView,CustomAuthToken

urlpatterns = [
    path("bookcreate/",bookCreateView.as_view(),name="create"),
    path("bookupdate/<int:pk>",bookUpdateView.as_view(),name="update"),
    path("bookdetails/<int:pk>",bookDetailView.as_view(),name="details"),
    path("booklist/",bookListView.as_view(),name="list"),
    path("delete/<int:pk>",bookDeleteView.as_view(),name="delete"),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

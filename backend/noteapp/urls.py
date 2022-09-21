"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import getNotes,getNote,updateNote,deleteNote,createNote

urlpatterns = [
    path('',getNotes,name='notes'),
    path('note/create',createNote,name='create-note'),
    path('notes/<int:pk>/',getNote,name='note'),
    path('notes/<int:pk>/update/',updateNote,name='update-note'),
    path('notes/<int:pk>/delete/',deleteNote,name='delete-note'),
]

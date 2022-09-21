
from multiprocessing import context
from django.shortcuts import render
# Create your views here.

from api.models import Notes


def getNotes(request):
    notes = Notes.objects.all()
    context = {
        'notes':notes
    }
    return render(request,'noteapp/notes.html',context)
def getNote(request,pk):
    note = Notes.objects.get(id=pk)
    context = {
        'note':note
    }
    return render(request,'noteapp/note.html',context)


def updateNote(request,pk):
    return render(request,'noteapp/base.html')

def deleteNote(request,pk):
    return render(request,'noteapp/base.html')


def createNote(request):
    return render(request,'noteapp/base.html')
   

from tkinter import N
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    
    routes = [{
        'Endpoint':'/notes/',
        'method':'POST',
        'body':None,
        'description':'Retund an array of notes'
    },
    {
        'Endpoint':'/notes/id',
        'method':'GET',
        'body':None,
        'description':'Retun a single note object'
    },
    {
        'Endpoint':'/notes/create',
        'method':'POST',
        'body':{'body':''},
        'description':'Creates new notes with data sent in post request'
    },
    {
        'Endpoint':'/notes/id/updated',
        'method':'PUT',
        'body':{'body':''},
        'description':'Creates an existing notes with data sent in post request'
    },
    {
        'Endpoint':'/notes/id/delete',
        'method':'DELETE',
        'body':None,
        'description':'Deleting and existing note'
    }]
    
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all().order_by('-update')
    serializer = NoteSerializer(notes,many = True)
    return  Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note,many = False)
    return  Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance = note,data=data)
    
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    
    return  Response('Note was deleted')

@api_view(['POST'])
def createNote(request):
    date = request.data
    note = Notes.objects.create(body = date['body'])
    serializer = NoteSerializer(note,many = False)
    return  Response(serializer.data)
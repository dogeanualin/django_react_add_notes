from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Notes

class NoteSerializer(ModelSerializer):
    class  Meta:
        model = Notes
        # fields =['body']
        fields = '__all__'

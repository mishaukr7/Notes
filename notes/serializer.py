from rest_framework import serializers
from .models import *


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['created', 'note_text']

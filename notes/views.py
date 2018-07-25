from .serializer import NoteSerializer
from .models import Note
from rest_framework import response, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from collections import Counter
import re
from django.shortcuts import HttpResponseRedirect


def get_uniq_len(data):
    return len(Counter(map(str.lower, re.findall(r"[\w']+", data))))


class NoteView(APIView):

    template_name = 'notes/note.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        sorted_serializer = sorted(serializer.data,
                                   key=lambda x: len(Counter(map(str.lower, re.findall(r"[\w']+", x['note_text'])))),
                                   reverse=True)
        return response.Response({'serializer': sorted_serializer})

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(redirect_to='')
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















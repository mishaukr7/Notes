from django.contrib import admin
from django.urls import path
from notes.views import NoteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', NoteView.as_view(), name='note-list'),
]





















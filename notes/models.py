from django.db import models


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    note_text = models.TextField(max_length=1024, blank=False)

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return self.note_text, self.created




# models.py
from django.db import models
from columns.models import Column

class Cards(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    column = models.ForeignKey(Column, related_name='cards', on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)
    
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Max

class Column(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Column)
def update_column_positions(sender, instance, created, **kwargs):
    if created:
        max_position = Column.objects.aggregate(Max('position'))['position__max']
        if max_position is not None:
            instance.position = max_position + 1
            instance.save(update_fields=['position'])

from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length = 20)
    capacity = models.CharField(max_length = 5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
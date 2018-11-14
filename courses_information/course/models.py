from django.db import models
from lecture.models import Lecture
from room.models import Room
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 40)
    tipe = models.CharField(max_length = 20)
    start = models.CharField(max_length = 5)
    end = models.CharField(max_length = 5)
    lecture = models.ForeignKey(Lecture, on_delete = models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, null=True)
    


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'
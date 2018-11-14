from django.db import models

# Create your models here.

class Lecture(models.Model):
    nip = models.CharField(max_length=15)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)

    def __str__ (self):
        return '%s : %s'%(self.nip, self.name)

    class Meta:
        db_table = 'lecture'
from django.db import models
from django.utils.text import slugify

class Handphone(models.Model):
    merk = models.CharField(max_length=200)
    tipe = models.CharField(max_length=100)
    about = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable = False)

    def save(self):
        self.slug = slugify(self.tipe)
        super(Handphone, self).save()    

    def __str__(self):        
        return "{}.{}({})".format(self.id, self.tipe, self.merk)    
    
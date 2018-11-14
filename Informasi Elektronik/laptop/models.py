from django.db import models
from django.utils.text import slugify

class Laptop(models.Model):
    merk = models.CharField(max_length=200)
    tipe = models.CharField(max_length=200)
    spesifikasi = models.TextField()
    harga = models.CharField(("Harga Barang"), max_length=50)
    publish = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):        
        self.slug = slugify(self.tipe)
        super(Laptop, self).save()
    def __str__(self):
        return "{}.{}({})".format(self.id, self.tipe,self.merk)

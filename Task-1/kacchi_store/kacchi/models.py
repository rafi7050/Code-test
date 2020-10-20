from django.db import models

# Create your models here.

class kacchi(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('kacchi_edit', kwargs={'pk': self.pk})



class sells(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    kacchi = models.ForeignKey(kacchi, on_delete=models.CASCADE)
    number_of_plates = models.DecimalField( decimal_places=2, max_digits=8)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    date_time = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.code
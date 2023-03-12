from django.db import models
from django.urls import reverse
# Create your models here.
class group(models.Model):
    name=models.CharField(max_length=10)
    notice=models.TextField(null=True,blank=True)
    date=models.DateField(null=True, blank=True)

    def get_absolute_url(self):
    #返回带id的url
        return reverse('catalog:group_detail', args=[str(self.id)])
    def __str__(self):

        return self.name
    
    def get_update_url(self):
        return reverse('catalog:update', args=[str(self.id)])
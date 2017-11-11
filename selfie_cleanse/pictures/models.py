from django.db import models

class Selfies(models.Model):
    imageType = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/', null=True)

#    def __unicode__(self):
#	return self.name


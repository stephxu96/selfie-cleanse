from django.db import models

class Selfie(models.Model):
    SELFIE ='Selfie'
    NONSELFIE= 'Nonselfie'
    IMAGE_TYPE_CHOICES = (
	('Person', (
		(SELFIE),
		(NONSELFIE),
	    )
	),
	('Other', 'other'),
    )
    
    image_type = models.CharField(
	max_length = 10,
	choices = IMAGE_TYPE_CHOICES,
	default='Other',
    )
    image = models.ImageField(upload_to='uploads/')
    
    def get_imageType(self):
        return self.image_type in (self.SELFIE)
    


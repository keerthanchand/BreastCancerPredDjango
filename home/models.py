from django.db import models

class imageUpload(models.Model):
	image = models.ImageField(upload_to='images/')
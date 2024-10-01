from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Gallery(models.Model):
    image = CloudinaryField('image')

    def __str__(self):
        return f"Gallery Image {self.id}"


class AboutUsContent(models.Model):
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return "About Us Content"


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)  # Add a field for contact number
    area = models.CharField(max_length=100)  # Add a field for area
    message = models.TextField()
    image = CloudinaryField('image')


    def __str__(self):
        return f"{self.name} - {self.message}"


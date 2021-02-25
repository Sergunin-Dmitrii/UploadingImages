from django.db import models
from django.core.exceptions import ValidationError


# Size validation
def valid_image(image):
        file_size=image.size
        limit_kb=200
        if file_size > limit_kb * 1024:
            raise ValidationError ("Size of file exceeded. Image size must be less 200 Kb.")


class Image(models.Model):
    image = models.ImageField(blank=False, null=False, validators=[valid_image])
   
    def __str__(self):
        return self.image.name

    
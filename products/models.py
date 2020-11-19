from django.db import models


# Create your models here.
class Category(models.Model):
    # Overwrite the default django pluralisation \
    #  which adds an 's' to the model name
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

from django.db import models
# https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True,
                                      blank=True)
    default_country = CountryField(blank_label='Country',
                                   max_length=40,
                                   null=True,
                                   blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True,
                                        blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile
        UserProfile.objects.create(user=instance)
    # else existing profile just save
    instance.userprofile.save()

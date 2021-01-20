from django.db import models
# https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from products.models import Product


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=20,
                                  null=True,
                                  blank=True)
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


class Reviews(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    date = models.DateField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     related_name='reviews')
    product = models.ForeignKey(Product,
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name='reviews')
    comment = models.TextField(default=False,
                               null=False,
                               blank=False)

    def __str__(self):
        return self.comment

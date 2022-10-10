from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile") #permet d'utiliser le model User


#le decorateur @receiver fait parti des SIGNALS Django, c'est une technique qui informe un model (Profile) de la création/sauvegarde
# d'un autre model (User). Ainsi chaque fois qu'un user est créé un profile est créé
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)

#la methode save_user_profile est appelée après un update du user
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
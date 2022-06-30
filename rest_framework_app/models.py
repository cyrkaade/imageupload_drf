from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE
from .images import make_thumbnail, make_copy
from . import get_username
from secrets import token_hex
from django.core.validators import MaxValueValidator, MinValueValidator
from .helpers import delete_exp
from django_q.tasks import schedule
from django_q.models import Schedule

# Creating User model

class myUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    BASIC = "BASIC"
    PREMIUM = "PREMIUM"
    ENTERPRISE = "ENTERPRISE"


    TIER_CHOICES = (
        (BASIC, "Basic"),
        (PREMIUM, "Premium"),
        (ENTERPRISE, "Enterprise"),
    )
    tier = models.CharField(max_length=20,
                  choices=TIER_CHOICES,
                  default="Basic")
    small_thumbnail_size = models.PositiveIntegerField(default=200)
    medium_thumbnail_size = models.PositiveIntegerField(default=400)
    # admins can change user's default thumbnail sizes
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


# Creating the UploadImage model

class UploadImage(models.Model):

    original = models.ImageField('Original image', default='uploaded_media/PNG_transparency_demonstration_1.png')
    small = models.ImageField(blank=True, null=True)
    medium = models.ImageField(blank=True, null=True)
    expiring_image_url = models.ImageField(blank=True, null=True)
    expire_secs_only_for_enterprise = models.IntegerField(blank=True, null=True, validators = [MaxValueValidator(3000), MinValueValidator(300)])
    # expiresecs works only for enterprise tier users
    
    def save(self, *args, **kwargs):
        req = get_username.get_request()
        user1 = myUser.objects.filter(username=req.user.username)
        super(UploadImage, self).save(*args, **kwargs)
        for user in user1:
        
            if user.tier.lower() == 'premium':
                make_thumbnail(self.small, self.original, (user.small_thumbnail_size, user.small_thumbnail_size), 'small')
                make_thumbnail(self.medium, self.original, (user.medium_thumbnail_size, user.medium_thumbnail_size), 'medium')
                self.expire_secs_only_for_enterprise = None
                super(UploadImage, self).save()

            elif user.tier.lower() == 'enterprise':
                make_thumbnail(self.small, self.original, (user.small_thumbnail_size, user.small_thumbnail_size), 'small')
                make_thumbnail(self.medium, self.original, (user.medium_thumbnail_size, user.medium_thumbnail_size), 'medium')
                random_str = token_hex(16)
                make_copy(self.expiring_image_url, self.original, f'{random_str}')
                super(UploadImage, self).save()
                schedule(func='delete_exp', args=self.expiring_image_url,
                schedule_type=Schedule.MINUTES, minutes=int(self.expire_secs_only_for_enterprise))
                super(UploadImage, self).save()
            else:
                self.small = None
                self.medium = None
                self.expire_secs_only_for_enterprise = None
                super(UploadImage, self).save()
        
        # save for thumbnail and icon
        # The one thing that i couldn't do was multiple image uploading. I tried to do it in multiple ways, but nothing changed. 
    
    


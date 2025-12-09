from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    is_active = models.BooleanField(default=True)
    user_type_choices = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    type = models.CharField(
        max_length=10,
        choices=user_type_choices,
        default='public',
        null=True,
        blank=True
    )
    date_made = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='new_profile/unknown.png')
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=40)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Unknown')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U', null=True, blank=True)
    follower = models.ManyToManyField(User, related_name='followers', blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
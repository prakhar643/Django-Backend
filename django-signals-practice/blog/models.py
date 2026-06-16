from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title
    

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    )

    model_name = models.CharField(max_length=100)
    object_id = models.IntegerField(null=True,blank=True)
    action = models.CharField(max_length=10,choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.model_name} - {self.action}"
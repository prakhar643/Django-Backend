from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserPlan(models.Model):
    PLAN_CHOICES = [
        ('free','Free'),
        ('premium','Premium')
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    plan = models.CharField(max_length=20,choices=PLAN_CHOICES,default='free')

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
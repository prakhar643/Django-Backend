from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import BlogPost
from django.utils.text import slugify


@receiver(pre_save, sender=BlogPost)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
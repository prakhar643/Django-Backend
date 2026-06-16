from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import BlogPost
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog
from .middleware import get_current_user
from django.contrib.auth.models import User
from blog.models import BlogPost


@receiver(pre_save, sender=BlogPost)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


# @receiver(post_save,sender=BlogPost)
# def generate_auto_profile(sender,instance,created,**kwargs):


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=BlogPost)
def log_blog_save(sender, instance, created, **kwargs):
    user = get_current_user()

    AuditLog.objects.create(
        model_name="BlogPost",
        object_id=instance.id,
        action="CREATE" if created else "UPDATE",
        user=user
    )


@receiver(post_delete, sender=BlogPost)
def log_blog_delete(sender, instance, **kwargs):
    user = get_current_user()

    AuditLog.objects.create(
        model_name="BlogPost",
        object_id=instance.id,
        action="DELETE",
        user=user
    )
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title
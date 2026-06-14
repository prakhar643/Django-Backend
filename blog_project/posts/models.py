from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()



class BlogPostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_at__isnull = False)
    
    def by_author(self, user):
        return self.filter(author = user)


    def trending(self):
        return self.order_by('-views')



class BlogPostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True,blank=True)
    views = models.IntegerField(default=0)

    objects = BlogPostQuerySet.as_manager()

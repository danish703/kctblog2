from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
    comment_msg = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_msg

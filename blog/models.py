from django.db import models

# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title




class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models
from registration.models import User
# Create your models here.


class comment(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    comts = models.TextField()

class Post(models.Model):
    # username = models.OneToOneField(User, on_delete = models.CASCADE,primary_key=True)
    # username = models.CharField(max_length=20)
    caption = models.TextField()
    post1 = models.ImageField(upload_to='images/',null=True,blank=True)
    # comments = models.ManyToManyField(comment)
    like = models.IntegerField()

    class Meta:
        verbose_name_plural = "All Post"

    # class Meta:
    #     unique_together = ("name", "year", )

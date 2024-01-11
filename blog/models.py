from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavePost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

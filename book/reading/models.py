from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    contents = models.TextField()
    price = models.CharField(max_length = 20)
    score = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    rating = models.CharField(max_length = 5, choices = score, default = '3', )
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()

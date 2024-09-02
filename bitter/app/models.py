from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.username.username

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to="tweet_photos/")
    created_at = models.DateField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:10]


class Saved(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username+'  '+self.tweet.text[:10]
    

class Liked(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username+'  '+self.tweet.text[:10]
    


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.username.username+'  '+self.comment

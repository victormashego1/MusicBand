from django.db import models


# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Choice(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

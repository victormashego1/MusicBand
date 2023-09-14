from django.db import models


# Create your models here.
class Music(models.Model):
    """Models are used to describe the data that must be stored for our app.
    Each attribute/variable of the model represents a database field.

    Music class variables : title, author, pub_date and image

    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        """The __str__() method returns a string representation of an object.

           :return: title
        """
        return self.title


class Choice(models.Model):
    """Models are used to describe the data that must be stored for our app.
       Each attribute/variable of the model represents a database field.

       Choice class variables : music, choice_text and votes

    """
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """The __str__() method returns a string representation of an object.

            :return: choice_text
        """
        return self.choice_text

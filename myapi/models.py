from django.db import models

# Create your models here.
#class Author(models.Model):
    #name=models.CharField(max_length=30)
    

class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    #author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
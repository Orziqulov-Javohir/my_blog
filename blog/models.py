from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from datetime import datetime
from django.core.validators  import MinLengthValidator, MaxLengthValidator
from django.db.models.fields import related

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,  null=True, blank=True, related_name='posts')
    slug = models.SlugField(unique=True, db_index=True, null=True)
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(800)], null=True)
    caption = models.ManyToManyField(Tag)
    

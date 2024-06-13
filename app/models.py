from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Musik(models.Model):
    title = models.CharField(max_length=228)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/new_images')
    audio = models.FileField(upload_to='media/news_audio')

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    view = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    view = models.IntegerField(default=10)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Our_team(models.Model):
    name = models.CharField(max_length=30)
    skill = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='teams')
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
    
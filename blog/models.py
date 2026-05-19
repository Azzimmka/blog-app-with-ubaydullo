from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    view = models.IntegerField(default=10, null=False, blank=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # type: ignore

    def __str__(self):
        return self.title


class Our_team(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    skill = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='teams', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
    
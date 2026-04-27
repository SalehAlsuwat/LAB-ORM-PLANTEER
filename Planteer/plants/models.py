from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plant(models.Model):

    class TextChoices(models.TextChoices):
        INDOOR = 'Indoor', 'indoor'
        OUTDOOR = 'Outdoor', 'outdoor'
        SUCCULENT = 'Succulent', 'succulent'
        FLOWERING = 'Flowering', 'flowering'
        HERB = 'Herb', 'herb'
        TREE = 'Tree', 'tree'
        SHRUB = 'Shrub', 'shrub'
        CACTUS = 'Cactus', 'cactus'
        FERN = 'Fern', 'fern'
        GRASS = 'Grass', 'grass'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=20, choices=TextChoices.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    countries = models.ManyToManyField('Country', related_name='plants')

    def __str__(self):
        return self.name


class Review(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


class Country(models.Model):
    name = models.CharField(max_length=32)
    flag = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.name
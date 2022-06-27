from django.db import models


class Category(models.Model):
    title= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Platform(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Raiting(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    platforma = models.ForeignKey(Platform, on_delete=models.CASCADE)
    raiting = models.ForeignKey(Raiting, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
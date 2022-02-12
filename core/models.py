from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Word(models.Model):
    spanish = models.CharField(max_length=50)
    dutch = models.CharField(max_length=50)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}: {self.spanish} / {self.dutch}"

    class Meta:
        ordering = ["category", "spanish"]

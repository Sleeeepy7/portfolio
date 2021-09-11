from django.db import models


# Create your models here.

class AboutModel(models.Model):
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "about me"


class ServiceModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="about service")

    def __str__(self):
        return self.name


class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="What client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.title

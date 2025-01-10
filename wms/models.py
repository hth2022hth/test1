from django.db import models


# Create your models here.

class Warehouse(models.Model):
    name = models.CharField("仓库名称", max_length=32, unique=True)

    class Meta:
        verbose_name = "仓库"

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField("用户", max_length=32, unique=True)
    password = models.CharField("密码", max_length=32)

    def __str__(self):
        return self.username

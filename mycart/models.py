from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField(upload_to='pic', null=False, blank=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.description} - {self.category.name if self.category else 'No Category'}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    # product = models.CharField(max_length=255, null=False)
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username}"

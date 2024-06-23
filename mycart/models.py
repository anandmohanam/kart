
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
    total = models.FloatField(null=True)

    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order by {self.user.username}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)
    cvv = models.CharField(max_length=3, blank=True, null=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    shipping_address = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    reminder_note = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment {self.id} by {self.user.username}"
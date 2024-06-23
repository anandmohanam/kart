from django.contrib import admin
from mycart.models import Photo, Category, Order, Payment

# Register your models here.
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Payment)


class New_order(admin.ModelAdmin):
    list_display = ['user', 'ordered_at']


admin.site.register(Order, New_order)

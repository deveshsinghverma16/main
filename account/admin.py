from django.contrib import admin

from .models import foodModel,CartModel,OrdersModel

admin.site.register(foodModel)

admin.site.register(CartModel)
admin.site.register(OrdersModel)

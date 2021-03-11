from django.contrib import admin
from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ['item','number','total_price']
    #list_display = [field.name for field in Item._meta.fields]


    list_filter = ('client', 'guest', )

    class Meta:
        model = Cart

admin.site.register(Cart,CartAdmin)



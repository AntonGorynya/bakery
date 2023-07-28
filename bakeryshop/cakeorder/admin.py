from django.contrib import admin
from django.utils.html import format_html

from .models import Cake
from .models import Customer
from .models import Order 
from .models import Advertisement
from .models import Levels_number, Form, Topping, Berries, Decor


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'occasion',
        'price',
        'show_preview'
    ]
    readonly_fields = [
        'show_preview'
    ]

    def show_preview(self, obj):
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            height='200px',
            url=obj.image.url
        )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'phonenumber'
    ]
    search_fields = [
        'phonenumber'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'delivery_time',
        'delivery_comment',
    ]


admin.site.register(Levels_number)
admin.site.register(Form)
admin.site.register(Topping)
admin.site.register(Berries)
admin.site.register(Decor)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'link',
        'clicks'
    ]
    readonly_fields = [
        'link'
    ]
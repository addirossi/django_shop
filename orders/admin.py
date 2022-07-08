from django.contrib import admin

from .models import Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_sum']
    inlines = [OrderItemsInline]


admin.site.register(Order, OrderAdmin)


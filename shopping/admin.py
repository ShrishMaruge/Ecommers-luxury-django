# admin.py
from django.contrib import admin
from .models import Product, CartItem, ShippingDetail
from django.utils.html import format_html, format_html_join
from django.urls import reverse

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'reviews', 'category', 'stock')
    search_fields = ('name', 'category')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user', 'session_id')
    search_fields = ('product__name', 'user__username')
    list_filter = ('user',)

@admin.register(ShippingDetail)
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'shipping_method', 'created_at', 'user', 'ordered_products')
    search_fields = ('name', 'email', 'shipping_method', 'user__username')
    list_filter = ('shipping_method', 'created_at')
    readonly_fields = ('created_at',)

    def ordered_products(self, obj):
        # List all CartItems products for the user of this ShippingDetail
        if obj.user:
            items = CartItem.objects.filter(user=obj.user)
            if items.exists():
                return format_html(
                    "<ul>{}</ul>",
                    format_html_join(
                        "",
                        "<li>{} (Qty: {})</li>",
                        ((item.product.name, item.quantity) for item in items)
                    )
                )
        return "-"
    ordered_products.short_description = "Ordered Products"

from django.contrib import admin
from .models import Order, Item

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = ('movie', 'quantity', 'price')
    readonly_fields = ()

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'date', 'item_count')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'user__email', 'id')
    readonly_fields = ('date',)
    inlines = [ItemInline]
    
    def item_count(self, obj):
        return obj.item_set.count()
    item_count.short_description = 'Items in Order'
    
    fields = ('user', 'total', 'date')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'movie', 'quantity', 'price', 'total_price')
    list_filter = ('order__date', 'movie')
    search_fields = ('movie__name', 'order__user__username')
    list_editable = ('quantity', 'price')
    
    def total_price(self, obj):
        return obj.quantity * obj.price
    total_price.short_description = 'Total Price'

admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
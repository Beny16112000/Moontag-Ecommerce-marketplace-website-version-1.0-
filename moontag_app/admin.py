from django.contrib import admin
from moontag_app.models import Category,Color,Size,Brand,Product,ProductAttribute,Banner,CartOrder,CartOrderItems
# Register your models here.
admin.site.register(Brand)
admin.site.register(Size)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('text','image_tag')
admin.site.register(Banner, BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category, CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_tag')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','brand','color','size','status','is_featured') # its a tuple but i will remember the name list better
    list_editable = ('status','is_featured')
admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','color','size')
admin.site.register(ProductAttribute, ProductAttributeAdmin)

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user','total_amt','paid_status','order_dt')
admin.site.register(CartOrder, CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('in_num','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
from django.contrib import admin
from moontag_app.models import AccessRecord,Topic,Webpage,Category,Color,Size,Brand,Product
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','color','size','price','status') # its a tuple but i will remember the name list better
    list_editable = ('status',)


admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from  .models  import *
# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(SubCategory)
admin.site.register(Uom)
admin.site.register(Vendor)
admin.site.register(DelivPart)
admin.site.register(Invman)

admin.site.register(FinManager)
admin.site.register(Brand)
admin.site.register(adminl)

# Register your models here.

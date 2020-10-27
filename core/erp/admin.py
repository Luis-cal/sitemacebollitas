from django.contrib import admin
from core.erp.models import *
from core.models import BaseModel
from import_export import resources
from import_export. admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
    class  Meta:
        model= Category

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_dysplay =('name','desc')

     resource_class = CategoryResource


class ProductResource(resources.ModelResource):
    class  Meta:
        model= Product

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_dysplay =('name','unidad','cat','pvp','iva','pui')

     resource_class = ProductResource

class ClientResource(resources.ModelResource):
         class  Meta:
            model= Client

class ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_dysplay =('names','surnames','dni',' date_birthday','address',' gender')

     resource_class = ClientResource


class SaleResource(resources.ModelResource):
         class  Meta:
            model= Sale

class SaleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_dysplay =(' cli','date_joined','subtotal',' iva','total')

     resource_class = SaleResource


class DetSaleResource(resources.ModelResource):
         class  Meta:
            model= DetSale

class DetSaleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     list_dysplay =(' sale','prod','price',' cant','subtotal')

     resource_class = DetSaleResource

     


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(DetSale,DetSaleAdmin)

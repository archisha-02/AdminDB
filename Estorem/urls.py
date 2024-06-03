"""Estorem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from adminl import views
from django.views.generic.base import TemplateView
from django.conf import settings  
from django.urls import path, include 
from django.conf.urls.static import static 
from adminl.views import *


from django.conf import settings  
from django.urls import path, include 
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.index,name="admindb"),
    # path('invm',views.invm,name="inventory-manager"),
    path('admin/', admin.site.urls),
    re_path(r'^api/adminlog/$', views.adminl_list),
    re_path(r'^api/customer/$', views.custm_list),
    re_path(r'^api/customer/([0-9])$', views.custm_detail),
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json'), name='manifest.json'),
    re_path(r'^api/stock/([0-9])$', views.update_product),
    re_path(r'^api/product/$', views.prod_list),
    re_path(r'^api/product/([0-9])$', views.prod_detail),
   
    re_path(r'^api/category/$', views.categ_list),
    path('api/category/<int:id>', CategUpAPIView.as_view(), name='update'),
    
    re_path(r'^api/subcategory/$', views.subcateg_list),
    path('api/subcategory/<int:id>', SubcategUpAPIView.as_view(), name='update'),

    re_path(r'^api/brand/$', views.brand_list),
    path('api/brand/<int:id>', BrandUpAPIView.as_view(), name='update'),

    re_path(r'^api/delivpar/$', views.deliv_list),
    re_path(r'^api/delivpar/([0-9])$', views.deliv_detail),

    re_path(r'^api/invman/$', views.invm_list),
    re_path(r'^api/invman/([0-9])$', views.invm_detail),

    re_path(r'^api/finman/$', views.finman_list),
    path('api/finman/<int:id>', FinUpAPIView.as_view(), name='update'),

    re_path(r'^api/vendor/$', views.vendor_list),
    re_path(r'^api/vendor/([0-9])$', views.vendor_detail),

    re_path(r'^api/uom/$', views.uom_list),
    re_path(r'^api/uom/([0-9])$', views.uom_detail),

    re_path(r'^api/adminl/$', views.adminl_list),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


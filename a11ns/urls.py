from django.conf.urls import url, include
from django.contrib import admin
import aiins.views

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^MP_verify_w8aZ0590YyF0l3jw\.txt', TemplateView.as_view(template_name='MP_verify_w8aZ0590YyF0l3jw.txt')),
    url(r'^$', aiins.views.index, name='index'),
    url(r'^aiins/', include('aiins.urls')),
    #url(r'^sale/',  aiins.salesman_alert.salesman_index, name='salesman'),
    url(r'^admin/', include(admin.site.urls)),
]
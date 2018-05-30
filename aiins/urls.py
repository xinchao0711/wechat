from django.conf.urls import url
from django.contrib import admin
import views
import index
import job
import health
import family_struct
import family_finance
import travel
import result
import customer_info
import salesman_alert
import findUser
import customer_service
import addinfo
urlpatterns = [
       url(r'^index/$', views.index, name='index'),
       url(r'^index/senddata', index.sendData, name='sendData_index'),
       url(r'^job/senddata', job.sendData, name='sendData_job'),
       url(r'^health/senddata', health.sendData, name='sendData_health'),
       url(r'^family_struct/senddata', family_struct.sendData, name='sendData_family_struct'),
       url(r'^family_finance/senddata', family_finance.sendData, name='sendData_family_finance'),
       url(r'^travel/senddata', travel.sendData, name='sendData_travel'),
       url(r'^result/family_rec', result.family_rec, name='family_rec'),
       url(r'^result/children_rec', result.children_rec, name='children_rec'),
       url(r'^result/health_rec', result.health_rec, name='health_rec'),
       url(r'^result/travel_rec', result.travel_rec, name='travel_rec'),
	   url(r'^result/more_rec', result.more_rec, name='more_rec'),
    
       url(r'^test1/', views.index1, name='index1'),
       url(r'^job/', views.job, name='job'),
       url(r'^health/', views.health, name='health'),
       url(r'^family_struct/', views.family_struct, name='family_struct'),
       url(r'^family_finance/', views.family_finance, name='family_finance'),
       url(r'^travel/', views.travel, name='travel'),
       url(r'^customer_info/', customer_info.customer, name='customer'),
       url(r'^entersalesman/', salesman_alert.salesman_index, name='salesman'),
       url(r'^customer_service_pc/1', customer_service.index, name='customer_service'),
       url(r'^customer_service_pc/submitData/', addinfo.updateInfo, name='updateInfo'),
       url(r'^customer_service_pc/set_employee/', addinfo.updateEmployee, name='setEmployee'),
       url(r'^user/find_one', findUser.findById, name='findById'),
       url(r'^customer_service_pc/login', customer_service.login, name='login'),
       url(r'^customer_service_pc/service_home', findUser.findAll, name='service_home'),
       url(r'^employee_manange/customer_list/', salesman_alert.find_customer_by_employeeid, name='findCustoByEmployeeId'),
]
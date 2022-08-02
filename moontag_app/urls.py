from django.urls import path
from moontag_app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register1',views.register1,name='register1'),
    path('login1',views.login1,name='login1'),
    path('logout1',views.logout1,name='log_out1'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('usersdisplay',views.usersdisplay,name='usersdisplay'),
    path('productdisplay',views.productdisplay,name='productdisplay')
]




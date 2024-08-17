from django.urls import path,include
from rest_framework import routers
from website import views

#router=routers.DefaultRouter()
#router.register(r'records',views.RecordViewSet)


urlpatterns = [
    #path('',include(router.urls)),
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk><slug>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]

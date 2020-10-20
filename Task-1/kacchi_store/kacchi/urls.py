from django.urls import path
from .views import HomeTemplateView
from django.conf.urls import url
from core import views



urlpatterns = [

    url(r'^sells_create/$', views.sells_create, name='sells_create'),
    path('', views.kacchiList.as_view(), name='kacchi_list'),
    path('view/<int:pk>', views.kacchiDetail.as_view(), name='kacchi_view'),
    path('new', views.kacchiCreate.as_view(), name='kacchi_new'),
    path('edit/<int:pk>', views.kacchiUpdate.as_view(), name='kacchi_edit'),
    path('delete/<int:pk>', views.kacchiDelete.as_view(), name='kacchi_delete'),
   
]
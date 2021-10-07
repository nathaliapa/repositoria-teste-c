from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name = 'home'),
    path('paginas/',views.paginas, name ='paginas'),
    path('login/',views.paginas, name='login')
]
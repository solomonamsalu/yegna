from django.urls import path,include
from . import views
urlpatterns =[
    path('/home',views.list.as_view())

]
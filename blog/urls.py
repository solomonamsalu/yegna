from django.urls import path,include
from . import views
urlpatterns =[
    path('article',views.list.as_view(),name="articles"),
    path('',views.Home,name="home")

]
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('', views.home, name = "home"),
    path ('signup', views.signup, name="signup"),
    path ('signin', views.signin, name="signin"),
    path ('signout', views.signout, name="signout"),
    path ('incident', views.incident, name="incident"),
    ]

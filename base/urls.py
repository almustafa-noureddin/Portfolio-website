from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),]
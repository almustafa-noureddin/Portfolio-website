from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('projects/', views.ProjectView.as_view(), name="projects"),
	path('projects/<slug:slug>', views.ProjectDetailView.as_view(), name="project"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]
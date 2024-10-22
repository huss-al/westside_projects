from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),  # Route for the home page
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('about/', views.about_view, name='about'),  # Add URL pattern for the About Us page
    path('contact/', views.contact_view, name='contact'),
]
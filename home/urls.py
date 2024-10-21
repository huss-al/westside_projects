from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),  # Route for the home page
        path('what-we-do/', views.what_we_do, name='what_we_do'),

]
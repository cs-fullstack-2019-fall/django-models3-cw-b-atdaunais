from django.urls import path
from . import views

urlpatterns = [
    path('addBook/', views.addBook),
    path('all/', views.printAll),
    path('recentpub/', views.recentPub),
    path('genreChange/', views.changeGenre),
]
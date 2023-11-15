from django.urls import path
from . import views

urlpatterns = [
    path('drink/',views.drinks_api_view,name = "drinks_api_view")
]

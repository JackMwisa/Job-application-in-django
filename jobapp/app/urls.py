from django.urls import path
from app.views import hello
from app.views import facilities

urlpatterns = [

    path('', hello),
    path('services/', facilities)
]

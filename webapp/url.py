from django.urls import path

from .models import employees

from .views import load_employee,load_detail
urlpatterns = [
    path('post1/', load_employee),
    path('detail/<str:username>/', load_detail),

]
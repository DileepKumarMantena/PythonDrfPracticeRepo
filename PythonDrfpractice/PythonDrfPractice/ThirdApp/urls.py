from django.urls import path
from .views import *

urlpatterns = [
    path('bmi/', Bmi.as_view()),
    path('bmiget/', Get.as_view()),
    path('bmiid/<int:id>/', GetById.as_view()),
    # path('update/<int:id>/', Update.as_view()),
    path('delete/<int:id>/', Delete.as_view()),
    path('Update/<int:pk>/', Update.as_view())
]

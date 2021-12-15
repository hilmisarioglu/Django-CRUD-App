from django.urls import path
from .views import HomePage , student_list , student_add

urlpatterns = [
    path('', HomePage ),
    path('student_list/', student_list , name='student_list'),
    path('student_add/', student_add , name='student_add'),
]
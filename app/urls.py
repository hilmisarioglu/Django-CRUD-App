from django.urls import path
from .views import HomePage , student_list , student_add , student_detail, student_update , student_delete

urlpatterns = [
    path('', HomePage , name = 'home'),
    path('student_list/', student_list , name='student_list'),
    path('student_add/', student_add , name='student_add'),
    path('detail/<int:id>/', student_detail , name='student_detail'),
    path('update/<int:id>/', student_update , name='student_update'),
    path('delete/<int:id>/', student_delete , name='student_delete'),
]

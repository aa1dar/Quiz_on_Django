from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='start_page'),
    path('<int:pk>',views.get_result,name = 'questions_detail'),
    path('endpage',views.end_result,name = 'endpage'),

]

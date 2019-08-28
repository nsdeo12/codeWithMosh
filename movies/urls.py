from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('',views.index,name='index'),
    path('<movie_id>',views.detail,name='detail')
    ]

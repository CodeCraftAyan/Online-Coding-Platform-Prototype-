from django.urls import path
from . import views

urlpatterns = [

    path('<int:contest_id>/', views.join_contest, name="join_contest"),

]
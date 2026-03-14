from django.urls import path
from . import views

urlpatterns = [

    path('', views.contest_list, name="contest_list"),

    path('contest/<int:contest_id>/', views.contest_dashboard, name="contest_dashboard"),

    path('scoreboard/<int:contest_id>/', views.scoreboard, name="scoreboard"),

]

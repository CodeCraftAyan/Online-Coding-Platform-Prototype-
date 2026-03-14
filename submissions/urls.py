from django.urls import path
from . import views

urlpatterns = [

    path('<int:problem_id>/', views.submit_code, name="submit_code"),

    path('result/<int:submission_id>/', views.submission_detail, name="submission_detail"),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('view_problem/<int:id>', views.viewProblem, name="view_problem"),
    path('compile/<int:id>', views.compile, name="compile"),
    path('view_source_code/<int:id>', views.viewSourceCode, name="view_source_code"),
    path('view_video_link/<int:id>', views.viewVideoLink, name="view_video_link"),
    path('view_all_problems', views.viewAllProblems, name="view_all_problems"),
    path('register/', views.registerPage, name="register"),
   	path('login/', views.loginPage, name="login"),
   	path('logout/', views.logoutUser, name="logout"),
    path('facts/', views.facts, name="facts"), 
    path('news/', views.news, name="news"), 
]

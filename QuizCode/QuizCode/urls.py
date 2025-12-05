"""
URL configuration for QuizCode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Quizapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home_page , name='home_page'),
    path('subject/', views.subject_list,name='subject_list'),
 
    path('quiz/<int:subject_id>', views.quiz,name='quiz'),
 
    path('add_new_question', views.add_new_question,name='add_new_question'),
    path('add_new_subject', views.add_new_subject,name='add_new_subject'),
    path('delete_subject/<int:del_id>', views.delete_subject, name='delete_subject'),
    
    path('subject/<str:xyz>/', views.invalid_url, name='invalid_url'),
    path('quiz/<int:subject_id>/<str:xyz>/', views.invalid_url, name='invalid_url'),
    path('add_new_question/<str:xyz>/', views.invalid_url, name='invalid_url'),
    path('add_new_subject/<str:xyz>/', views.invalid_url, name='invalid_url'),
    path('delete_subject/<int:del_id>/<str:xyz>/', views.invalid_url, name='invalid_url'),
    path('<str:xyz>/', views.invalid_url, name='invalid_url')


]

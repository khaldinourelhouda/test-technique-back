"""authentification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include,path
from rest_framework import routers
from testdb import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategorieViewSet, basename='Categorie')
urlpatterns = [
    path('', include(router.urls)),
    path('tests', views.TestListView.as_view(), name="tests"),
    path('testcreate', views.TestCreateView.as_view(), name="testcreate"),
    path('questions', views.QuestionListView.as_view(), name="questions"),
    path('reponses', views.ReponseListView.as_view(), name="reponses"),
    path('reponse/', views.QuestionReponseView.as_view()),
    path('reponsecreate/', views.ReponseCreateView.as_view()),
    path('questionscreate', views.QuestionCreateView.as_view()),
    path('questionsreponsecreate', views.QuestionReponseCreateView.as_view()),
    path('choix_utilisateur', views.Choix_UtilisateurListView.as_view(), name="choix_utilisateur"),
    path('utilisateur_test', views.Utilisateur_TestListView.as_view(), name="utilisateur_test"),
    path('utilisateur_testread', views.Utilisateur_TestreadListView.as_view(), name="utilisateur_test"),
    path('users', views.UtilisateurListView.as_view(), name="users"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/login/', include('authemail.urls')),
 
]

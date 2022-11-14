from django.urls import path
from . import views

urlpatterns = [
    path('diseasesearch', views.diseasesearch, name = 'autocomplete_diseases'),
    path('snpsearch', views.snpsearch, name = 'autocomplete_snp'),
    path('genesearch', views.genesearch, name = 'autocomplete_gene'),
    path('login_user', views.login_users, name = 'login'),
    path('logout_user',views.logout_user, name = 'logout'),
    path('register_user',views.register_user, name = 'register_user'),

]
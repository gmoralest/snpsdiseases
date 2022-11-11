from django.urls import path
from . import views

urlpatterns = [
    path('diseasesearch', views.diseasesearch, name = 'autocomplete_diseases'),
    path('snpsearch', views.snpsearch, name = 'autocomplete_snp'),
    path('genesearch', views.genesearch, name = 'autocomplete_gene'),

]
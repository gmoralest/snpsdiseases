"""snpsdiseases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from snpsdiseasesapp.views import genesearch, homepage, database, diseasesearch,disease_search_result,snpsearch,snp_search_result, ItemListView_Snp2Phenotype2Ref ,ItemListView_Snp, ItemListView_Reference, ItemListView_DiseaseTrait, ItemListView_Genes
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('homepage/', homepage),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    
    
    path('genesearch/', genesearch),


    path('homepage/Snpsearch/', snpsearch),
    path('homepage/Snpsearchresults/', snp_search_result),

    path('homepage/diseasesearch/', diseasesearch),
    path('homepage/diseasesearchresults/', disease_search_result),
    
    path('', include('snpsdiseasesapp.urls')),    
    
    path('database/', database),
    path('database/Snp2Phenotype2Ref', ItemListView_Snp2Phenotype2Ref.as_view()),
    path('database/Snp', ItemListView_Snp.as_view()),
    path('database/Reference', ItemListView_Reference.as_view()),
    path('database/DiseaseTrait', ItemListView_DiseaseTrait.as_view()),
    path('database/Genes', ItemListView_Genes.as_view()),  
]
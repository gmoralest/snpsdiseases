from django.contrib import admin
from django.urls import path, include
from snpsdiseasesapp.views import genesearch,genesearchresults, homepage, database, diseasesearch,disease_search_result,snpsearch,snp_search_result, ItemListView_Snp2Phenotype2Ref ,ItemListView_Snp, ItemListView_Reference, ItemListView_DiseaseTrait, ItemListView_Genes,faqs_page,individualsnp, individualreference
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('homepage/', homepage, name = 'home'),
    path('',include('django.contrib.auth.urls')),
    path('diseasesearch/', diseasesearch, name = 'diseasesearch'),
    path('diseasesearchresults/', disease_search_result, name = 'diseasesearchresult'),
    path('Snpsearch/', snpsearch, name = 'snpsearch'),
    path('snpsearchresults/', snp_search_result, name = 'snpsearchresult'),
    path('genesearch/', genesearch, name = 'genesearch'),
    path('genesearchresults/', genesearchresults, name = 'genesearchresult'),
    path('', include('snpsdiseasesapp.urls')),    
    path('database/', database, name = 'database'),
    path('database/Snp2Phenotype2Ref', ItemListView_Snp2Phenotype2Ref.as_view()),
    path('database/Snp', ItemListView_Snp.as_view()),
    path('database/Reference', ItemListView_Reference.as_view()),
    path('database/DiseaseTrait', ItemListView_DiseaseTrait.as_view()),
    path('database/Genes', ItemListView_Genes.as_view()),
    path('faqs/',faqs_page,name = 'faqs'),
    path('individualsnp/<int:id>/', individualsnp, name='individualsnp'),
    path('individualreference/<int:reference>/', individualreference, name='individualreference'),  
]
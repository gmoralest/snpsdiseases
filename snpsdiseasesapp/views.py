from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from snpsdiseasesapp.models import Snp2Phenotype2Ref, DiseaseTrait,Reference,Snp, Genes


# Create your views here.
def homepage(request,):
    return render(request, 'homepage.html')

def login(request,):
    return render(request, 'login.html')

@login_required(login_url='/login')
def genesearch(request,):
    return render(request, 'genesearch.html')

def database(request,):
    return render(request,'database.html')

def diseasesearch(request,):
    if 'term' in request.GET:
        qs = DiseaseTrait.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for diseases in qs:
            names.append(diseases.name)
        return JsonResponse(names, safe=False)
    return render(request, 'diseasesearch.html')

def snp_search_result(request,):
    snp = request.GET['snp']
    chrom = request.GET['chrom']
    chrom_pos = request.GET['chrom_pos']
    print(snp)
    print(chrom)
    print(chrom_pos)
    #### VER COMO FILTRAR LAS QUERY QUE NO TIENEN RESULTADOS ####
    
    queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id = snp).values_list('id', 'snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment'))
    #t_queryset = list(zip(*queryset))
    columns = ['id', 'snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment']
    context = {}
    context["disease"] = snp
    context["data"] = queryset
    context["columns"] = columns
    return render(request, 'diseasesearchresult.html', context = context)

def snpsearch(request,):
    if 'term' in request.GET:
        qs = Snp.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for diseases in qs:
            names.append(diseases.name)
        return JsonResponse(names, safe=False)
    return render(request, 'snpsearch.html')

def disease_search_result(request,):
    disease = request.GET['disease']
    queryset = list(Snp2Phenotype2Ref.objects.filter(disease_trait_id = disease).values_list('id', 'snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment'))
    #t_queryset = list(zip(*queryset))
    columns = ['id', 'snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment']
    context = {}
    context["disease"] = disease
    context["data"] = queryset
    context["columns"] = columns
    return render(request, 'diseasesearchresult.html', context = context)



def snpsearch(request,):
    if 'term' in request.GET:
        qs = Snp.objects.filter(rsid__icontains=request.GET.get('term'))
        names = list()
        for snp in qs:
            names.append(str(snp.rsid))
        return JsonResponse(names, safe=False)
    return render(request, 'snpsearch.html')



from django_serverside_datatable.views import ServerSideDatatableView

class ItemListView_Snp2Phenotype2Ref(ServerSideDatatableView):
    queryset = Snp2Phenotype2Ref.objects.all()
    columns = ['id', 'snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment']

class ItemListView_Snp(ServerSideDatatableView):
    queryset = Snp.objects.all()
    columns = ['rsid', 'chrom', 'chrom_pos']

class ItemListView_Reference(ServerSideDatatableView):
    queryset = Reference.objects.all()
    columns = ['pubmedid', 'journal', 'title','date','link']

class ItemListView_DiseaseTrait(ServerSideDatatableView):
    queryset = DiseaseTrait.objects.all()
    columns = ['name']

class ItemListView_Genes(ServerSideDatatableView):
    queryset = Genes.objects.all()
    columns = ['name']    



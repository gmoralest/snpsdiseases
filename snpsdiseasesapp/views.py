from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from snpsdiseasesapp.models import Snp2Phenotype2Ref, DiseaseTrait,Reference,Snp, Genes
from django.db.models import Prefetch
from .forms import RegisterUserForm

def login_users(request,):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)     
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('There was an error login in, try again'))
            return redirect('login')
    else:
        return render(request, 'registration/login.html',{})

def logout_user(request,):
    logout(request)
    messages.success(request,('You were Logged Out'))
    return redirect('home')

def register_user(request,):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, ("Resgistration Successfull"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request,'registration/register_user.html',{
        'form': form
    })


def homepage(request,):
    return render(request, 'homepage.html')

def genesearch(request,):
    if 'term' in request.GET:
        qs = Genes.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for genes in qs:
            names.append(genes.name)
        return JsonResponse(names, safe=False)
    return render(request, 'genesearch.html')

def genesearchresults(request,):
    gene = request.GET['gene']
    queryset = list(Snp2Phenotype2Ref.objects.filter(genes = gene).values_list('snp_id', 'disease_trait_id','genes','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
    data = []
    for element in queryset:
        dico = {'snp_id': element[0], 'disease_trait_id':element[1], 'genes':element[2],'reference_id':element[3],'chrom':element[4],'chrom_pos':element[5]}
        data.append(dico)
    columns = ['snp_id', 'disease_trait_id','genes','reference_id','snp_id__chrom', 'snp_id__chrom_pos']
    context = {}
    context["gene"] = gene
    context["data"] = data
    context["columns"] = columns
    return render(request, 'genesearchresult.html', context = context)


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
    chrom_selected = request.GET['chrom']
    chrom_pos_start = request.GET['chrom_pos_start']
    chrom_pos_end = request.GET['chrom_pos_end']
    if snp.isalnum() and len(snp)>0:
        queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id = snp).select_related('snp_id').values_list('snp_id', 'disease_trait_id','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
    else:     
        if chrom_selected.isalnum() and len(chrom_selected)>0:
            if chrom_pos_start.isalnum() and len(chrom_pos_start)>0 and chrom_pos_end.isalnum() and len(chrom_pos_end)>0:
                queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id__chrom = chrom_selected, snp_id__chrom_pos__lte = chrom_pos_end, snp_id__chrom_pos__gte = chrom_pos_start).select_related('snp_id').values_list('snp_id', 'disease_trait_id','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
            else:
                if  chrom_pos_start.isalnum() and len(chrom_pos_start)>0:
                    queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id__chrom = chrom_selected, snp_id__chrom_pos__gte = chrom_pos_start).select_related('snp_id').values_list('snp_id', 'disease_trait_id','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
                else:       
                    if chrom_pos_end.isalnum() and len(chrom_pos_end)>0:
                       queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id__chrom = chrom_selected, snp_id__chrom_pos__lte = chrom_pos_end).select_related('snp_id').values_list('snp_id', 'disease_trait_id','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
                    else:
                        queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id__chrom = chrom_selected).select_related('snp_id').values_list('snp_id', 'disease_trait_id','reference_id','snp_id__chrom', 'snp_id__chrom_pos'))
    data = []
    for element in queryset:
        dico = {'snp_id': element[0], 'disease_trait_id':element[1], 'reference_id':element[2],'chrom':element[3],'chrom_pos':element[4]}
        data.append(dico)
    context = {}
    context["disease"] = snp
    context["data"] = data
    return render(request, 'snpsearchresult.html', context = context)

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
    queryset = list(Snp2Phenotype2Ref.objects.filter(disease_trait_id = disease).values_list('snp_id', 'disease_trait_id','reference_id','pvalue','neg_log10_pvalue','comment'))
    data = []
    for element in queryset:
        dico = {'snp_id':element[0], 'disease_trait_id':element[1],'reference_id':element[2],'pvalue': '{:.2e}'.format(element[3]),'neg_log10_pvalue':round(element[4], 2),'comment':element[5]}
        data.append(dico)
    context = {}
    context["disease"] = disease
    context["data"] = data
    return render(request, 'diseasesearchresult.html', context = context)


def snpsearch(request,):
    if 'term' in request.GET:
        qs = Snp.objects.filter(rsid__icontains=request.GET.get('term'))
        names = list()
        for snp in qs:
            names.append(str(snp.rsid))
        return JsonResponse(names, safe=False)
    return render(request, 'snpsearch.html')

def faqs_page(request):
    return render(request, 'faqs.html')

def individualsnp(request, id):
    queryset = list(Snp2Phenotype2Ref.objects.filter(snp_id = id).select_related('reference_id').select_related('snp_id').select_related('genes').values_list('snp_id', 'disease_trait_id', 'snp_id__chrom','snp_id__chrom_pos' , 'reference_id__title', 'reference_id__link'))
    data = []
    for element in queryset:
        dico = {'snp_idd': element[0], 'disease_trait_id':element[1], 'chrom':element[2],'chrom_pos':element[3],'title':element[4],'link':element[5]}
        data.append(dico)
    context = {}
    context['snp'] = id
    context['data'] = data
    return render(request, 'individualsnp.html', context = context)

def individualreference(request,reference):
    queryset = list(Snp2Phenotype2Ref.objects.filter(reference_id = reference).select_related('reference_id').select_related('snp_id').select_related('genes').values_list('snp_id', 'disease_trait_id','reference_id','reference_id__journal', 'reference_id__title', 'reference_id__date', 'reference_id__link'))
    data = []
    for element in queryset:
        dico = {'snp_id': element[0], 'disease_trait_id':element[1], 'reference_id':element[2],'journal':element[3],'title':element[4],'date':element[5],'link':element[6]}
        data.append(dico)
    context = {}
    context['reference'] = reference
    context['data'] = data
    return render(request, 'individualreference.html', context = context)


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
 



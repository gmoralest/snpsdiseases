from django.contrib import admin
from .models import Snp, Reference, DiseaseTrait, Snp2Phenotype2Ref

admin.site.register(Snp)

admin.site.register(Reference)

admin.site.register(DiseaseTrait)

admin.site.register(Snp2Phenotype2Ref)
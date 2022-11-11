## DATA SEARCH ##

import pandas as pd

data= pd.read_csv("/home/gabi/MASTER/bio_info/M2/programation web/snpsdiseases/gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_100000.tsv" ,sep='\t', dtype='unicode')


# # ## GET ALL unique SNP IN THE TABLE I
# snps_ids = data['SNP_ID_CURRENT'].unique()
# print(snps_ids.shape)
# for id in snps_ids:
#     line = data.loc[data['SNP_ID_CURRENT'] == id].iloc[0][['SNP_ID_CURRENT','CHR_ID','CHR_POS']]
#     p = Snp(chrom = line['CHR_ID'], chrom_pos = line['CHR_POS'], rsid = line['SNP_ID_CURRENT'])
#     p.save()

# # GET ALL THE References IN THE TABLE
# references_ids = data['PUBMEDID'].unique()
# for id in references_ids:
#     line = data.loc[data['PUBMEDID'] == id].iloc[0][['PUBMEDID','JOURNAL','STUDY','DATE','LINK']]
#     p = Reference(pubmedid = line['PUBMEDID'], journal = line['JOURNAL'], title = line['STUDY'], date = line['DATE'], link = line['LINK'])
#     p.save()

# GET ALL THE DISEASES IN THE TABLE
# diseasetrait_list = data['DISEASE/TRAIT'].unique()
# for disease in diseasetrait_list:
#     p = DiseaseTrait(name = disease)
#     p.save()

# # GET ALL THE GENES IN THE TABLE
# genes_list_raw = data['SNP_GENE_IDS']
# gene_list_unique = []
# for gene in genes_list_raw:
#     if type(gene) == float:
#         pass
#     else:
#         splitted_gene = gene.split(", ")
#         for i in splitted_gene:
#             if i not in gene_list_unique:
#                 gene_list_unique.append(i)
# print(len(gene_list_unique))

# for row in range(0,data.shape[0]):
#     line = data.iloc[row][['SNP_ID_CURRENT','DISEASE/TRAIT','PUBMEDID','P-VALUE', 'PVALUE_MLOG','P-VALUE (TEXT)']]
#     disease_row= DiseaseTrait.objects.get(name = line['DISEASE/TRAIT'])
#     snp_row = Snp.objects.get(rsid = line['SNP_ID_CURRENT'])
#     reference_row = Reference.objects.get(pubmedid = line['PUBMEDID'])
#     p = Snp2Phenotype2Ref(snp_id = snp_row, disease_trait_id = disease_row,
#                     reference_id = reference_row ,pvalue = line['P-VALUE'],
#                     neg_log10_pvalue = line['PVALUE_MLOG'], comment = line['P-VALUE (TEXT)'])
#     p.save() 
                   
# Snp.objects.get(rsid = )
# Reference.objects.get(pubmedid = )



# # class Snp2Phenotype2Ref(models.Model):
# AUTOINCREMENT
# #     id = models.IntegerField()

# #     snp_id = models.IntegerField()
# #     disease_trait_id = models.IntegerField()
# #     reference_id = models.IntegerField()
# #     pvalue = models.FloatField()
# #     neg_log10_pvalue = models.FloatField()


## DATABASE FILLING ###

import pandas as pd
from snpsdiseasesapp.models import Snp, DiseaseTrait, Reference, Snp2Phenotype2Ref, Genes

data= pd.read_csv("/home/gabi/MASTER/bio_info/M2/programation web/snpsdiseases/gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_100000.tsv" ,sep='\t', dtype='unicode')


# # ## GET ALL unique SNP IN THE TABLE I
snps_ids = data['SNP_ID_CURRENT'].unique()
for id in snps_ids:
    line = data.loc[data['SNP_ID_CURRENT'] == id].iloc[0][['SNP_ID_CURRENT','CHR_ID','CHR_POS']]
    p = Snp(chrom = line['CHR_ID'], chrom_pos = line['CHR_POS'], rsid = line['SNP_ID_CURRENT'])
    p.save()

# # GET ALL THE References IN THE TABLE
references_ids = data['PUBMEDID'].unique()
for id in references_ids:
    line = data.loc[data['PUBMEDID'] == id].iloc[0][['PUBMEDID','JOURNAL','STUDY','DATE','LINK']]
    p = Reference(pubmedid = line['PUBMEDID'], journal = line['JOURNAL'], title = line['STUDY'], date = line['DATE'], link = line['LINK'])
    p.save()

# GET ALL THE DISEASES IN THE TABLE
diseasetrait_list = data['DISEASE/TRAIT'].unique()
for disease in diseasetrait_list:
    p = DiseaseTrait(name = disease)
    p.save()

# GET ALL THE GENES IN THE TABLE
genes_list_raw = data['SNP_GENE_IDS']
gene_list_unique = []
for gene in genes_list_raw:
    if type(gene) == float:
        pass
    else:
        splitted_gene = gene.split(", ")
        for i in splitted_gene:
            if i not in gene_list_unique:
                gene_list_unique.append(i)
for gene in gene_list_unique:
    p = Genes(name = gene)
    p.save()


for row in range(0,data.shape[0]):
    line = data.iloc[row][['SNP_ID_CURRENT','DISEASE/TRAIT','PUBMEDID','P-VALUE', 'PVALUE_MLOG','P-VALUE (TEXT)','SNP_GENE_IDS']]
    disease_row= DiseaseTrait.objects.get(name = line['DISEASE/TRAIT'])
    snp_row = Snp.objects.get(rsid = line['SNP_ID_CURRENT'])
    reference_row = Reference.objects.get(pubmedid = line['PUBMEDID'])
    gene_row_raw = genes = line['SNP_GENE_IDS']
    p = Snp2Phenotype2Ref.objects.create(snp_id = snp_row, disease_trait_id = disease_row,
                    reference_id = reference_row ,pvalue = line['P-VALUE'],
                    neg_log10_pvalue = line['PVALUE_MLOG'], comment = line['P-VALUE (TEXT)'])
    if type(gene_row_raw) == str:
        splitted_gene = gene_row_raw.split(", ")
        for gene in splitted_gene:
            p.genes.add(gene)
    p.save()
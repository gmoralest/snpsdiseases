from django.db import models

# Create your models here.
class Snp(models.Model):
    rsid = models.IntegerField(primary_key=True)
    chrom = models.CharField(max_length= 50)
    chrom_pos = models.CharField(max_length= 50)

    class Meta:
        ordering = ['rsid']

    def __str__(self):
        return self.rsid

class Reference(models.Model):
    pubmedid =  models.IntegerField(primary_key=True)
    journal = models.CharField(max_length= 50)
    title = models.CharField(max_length=200)
    date = models.DateField()
    link = models.CharField(max_length=200, default= None, editable=True)

    class Meta:
        ordering = ['pubmedid']

    def __str__(self):
        return self.pubmedid

class DiseaseTrait(models.Model):
    name = models.CharField(max_length= 200,primary_key=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Genes(models.Model):
    name = models.CharField(max_length= 20,primary_key=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Snp2Phenotype2Ref(models.Model):
    id = models.AutoField(primary_key=True)
    snp_id = models.ForeignKey(Snp,on_delete = models.CASCADE)
    disease_trait_id = models.ForeignKey(DiseaseTrait,on_delete = models.CASCADE)
    reference_id = models.ForeignKey(Reference,on_delete = models.CASCADE)
    genes = models.ManyToManyField(Genes, blank=True)
    pvalue = models.FloatField()
    neg_log10_pvalue = models.FloatField()
    comment = models.CharField(max_length=200, editable=True, default=None) 
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


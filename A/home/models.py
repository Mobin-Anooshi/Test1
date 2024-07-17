from django.db import models

# Create your models here.


class Companies(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name =models.ForeignKey(Companies , on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    number = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.company_name

class CompanyAssembly(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class CompanyPeople(models.Model):
    company = models.ForeignKey(CompanyAssembly , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name


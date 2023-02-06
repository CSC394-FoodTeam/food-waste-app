from django.db import models

# Create your models here.

class Inventory(models.Model):
    item_name = models.CharField(max_length=30)
    quantity_of_item = models.IntegerField()
    #expiration_date = models.DateField(blank=True)
    
    def __str__(self) -> str:
        return self.item_name + ": " + str(self.quantity_of_item) #+ ": " + str(self.expiration_date)

class Fridge(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    quantity = models.IntegerField()
    exp_date = models.DateField(null=True)


    def __str__(self) -> str:
        return self.name + " : " + str(self.quantity) + " : " + str(self.exp_date)

class Pantry(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    quantity = models.IntegerField()
    exp_date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name + " : " + str(self.quantity) + " : " + str(self.exp_date)
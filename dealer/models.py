from django.db import models

class Citie(models.Model):
    Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class Categorie(models.Model):
    Type=models.CharField(max_length=50)
    def __str__(self):
        return self.Type

class Offer(models.Model):
    Discount=models.CharField(max_length=50)
    def __str__(self):
        return self.Discount

class Bedroom(models.Model):
    Number=models.CharField(max_length=50)
    def __str__(self):
        return str(self.Number)

class Bathroom(models.Model):
    Number=models.CharField(max_length=50)
    def __str__(self):
        return str(self.Number)

class Area(models.Model):
    Unit=models.CharField(max_length=50)
    Number=models.IntegerField(default=0)
    def __str__(self):
        return str(self.Number)+str(" ")+str(self.Unit)

class Property(models.Model):
    name=models.CharField(max_length=255,blank=True)
    Categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='Categorie')
    City=models.ForeignKey(Citie,on_delete=models.CASCADE,related_name='City')
    Offer=models.ForeignKey(Offer,on_delete=models.CASCADE,related_name='Offer')
    Bedrooms=models.ForeignKey(Bedroom,on_delete=models.CASCADE,related_name='Bedrooms')
    Bathrooms=models.ForeignKey(Bathroom,on_delete=models.CASCADE,related_name='Bathrooms')
    Area=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='Area')
    image=models.ImageField(upload_to="media",blank=True)
    Price_Unit=models.CharField(null=True,max_length=50)
    price=models.FloatField(default=0)
    def __str__(self):
        return str(self.Area)+str(" at ")+str(self.City)

class Mail(models.Model):
    Email=models.EmailField()

    def __str__(self):
        return str(self.Email)
    

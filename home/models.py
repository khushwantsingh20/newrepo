from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
PRODUCT_CHOICES = (
        ('phone', 'Phone'),
        ('laptop', 'Laptop'),
        ('keyboard', 'Keyboard'),
        ('book', 'Book'),
        ('tshirt', 'T-Shirt'),
        ('pants', 'Pants'),
        ('mouse', 'Mouse'),
        ('shoes', 'Shoes'),
        ('bags', 'Bags'),
        ('toy', 'Toy'),
        ('electonics', 'Electronics'),
        ('kitchen', 'Kitchen')
        
    )
class Product(models.Model):
    id= models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to="pimg")
    desc = models.TextField()
    product_type = models.CharField(max_length=15, choices=PRODUCT_CHOICES, blank=True , null=True)
    stock=models.PositiveIntegerField(default=10)
    rating = models.PositiveIntegerField( default=1, validators=[MaxValueValidator(5),MinValueValidator(1)])

   
    
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


#admin
    def __str__(self):
        return self.name    



class Webimg(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="webimg")

    def __str__(self):
        return self.title
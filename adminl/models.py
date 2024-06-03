
from django.db import models
from django.db.models import Model



# class adminl(models.Model):
#     email = models.CharField(max_length=50,default='kartik@gmail.com')
#     password= models.CharField(max_length=50, default="fruits")

#     #to save the data
#     def register(self):
#         self.save()

class Category(models.Model):
    allowed= models.BooleanField(default=False)
    category= models.CharField(max_length=50, default="fruits")
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    color= models.CharField(max_length=10, default='', blank=True, null= True)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
 

class SubCategory(models.Model):
    subcategory= models.CharField(max_length=50)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    allowed= models.BooleanField(default=False)
    color= models.CharField(max_length=10, default='', blank=True, null= True)
    
    @staticmethod
    def get_all_subcategories():
        return Category.objects.all()
 
    
class Customer(models.Model):
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    agentimage = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    address= models.CharField(max_length=250, default='', blank=True, null= True)
    pin = models.CharField(max_length=10,default='000000')

    #to save the data
    def register(self):
        self.save()

class Uom(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Vendor(models.Model):
 
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    agentimage = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    state = models.CharField(max_length=50, default='', blank=True, null= True)
    address= models.CharField(max_length=250, default='', blank=True, null= True)

    


    #to save the data
    def register(self):
        self.save()

class Invman(models.Model):
 
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    agentimage = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    state = models.CharField(max_length=50, default='', blank=True, null= True)
    address= models.CharField(max_length=250, default='', blank=True, null= True)
    # orderId= models.CharField(max_length=10, default='abc')
    # password= models.CharField(max_length=50,default='test1234')
    
    
    

    #to save the data
    def register(self):
        self.save()

class DelivPart(models.Model):
 
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    agentimage = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    state = models.CharField(max_length=50, default='', blank=True, null= True)
    address= models.CharField(max_length=250, default='', blank=True, null= True)
    # orderId= models.ForeignKey(Invman,on_delete=models.CASCADE,default=1 )
    # password= models.CharField(max_length=50,default='test1234')
    



    #to save the data
    def register(self):
        self.save()

class FinManager(models.Model):
 
    firstname = models.CharField(max_length=50,default='Kartik')
    lastname = models.CharField (max_length=50,default='Singhania')
    contact = models.CharField(max_length=10)
    agentimage = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    email=models.EmailField(max_length=50,default='karsingh@gmail.com')
    city = models.CharField(max_length=50,default='Koregaon')
    state = models.CharField(max_length=50, default='', blank=True, null= True)
    address= models.CharField(max_length=250, default='', blank=True, null= True)
    

    #to save the data
    def register(self):
        self.save()



    
class Brand(models.Model):
    bname=models.CharField(max_length=50, default="Nike")
    vendors= models.ForeignKey(Vendor,on_delete=models.CASCADE,default=1 )

class Product(models.Model):
    productname = models.CharField(max_length=60,default="coldr")
    productprice= models.IntegerField(default=300)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    subcategory= models.CharField(max_length=50,default="milk")
    brand=models.CharField(max_length=50,default="PARLEG")
    uom=models.CharField(max_length=50,default="abc")
    offer=models.CharField(max_length=10,default='20%')
    quantity= models.IntegerField(default=10)
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
        
class adminl(models.Model):
 
    username = models.CharField(max_length=50,default='admin07')
    password = models.CharField(max_length=50,default='test1234')


    #to save the data
    def register(self):
        self.save()
        
class Update(models.Model):
    quantity= models.IntegerField(default=10)


# # Create your models here.

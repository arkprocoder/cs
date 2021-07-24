from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=50,primary_key=True)
    Emailaddress=models.CharField(max_length=50,default="")
    Address=models.CharField(max_length=50,default="")
    Location=models.CharField(max_length=50,default="")
    Universityname=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.Name()






    
    
    


     

     

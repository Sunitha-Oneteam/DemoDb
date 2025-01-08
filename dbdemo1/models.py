
from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=10)  
	address=models.CharField(max_length=50)
	age=models.IntegerField() 

	def __str__(self):
		return self.name 
		   
		








'''
The __str__ method just tells Django what to print 
 when it needs to print out an instance of any model

#Commands to create Model class
pip install mysqlclient

python manage.py makemigrations
python manage.py migrate


#Field Types in Django
IntegerField() ,
DecimalField(max_digits=3,decimal_places=2)         
BigIntegerField()
EmailField()
DateField()
DateTimeField()
TextField()
ImageField()

#from phonenumber_field.modelfields import PhoneNumberField

	#Phonenumber=PhoneNumberField(blank=True)
	
	
		

'''









'''
class Meta:
	db_table = 'dbdemo_employee'
To generate a unique random nbr in model class
import random
def create_new_ref_number():
      return str(random.randint(1000, 9999))
	uid=models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number())

	#age=models.IntegerField()
'''
	



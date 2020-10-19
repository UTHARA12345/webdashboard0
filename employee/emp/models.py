from django.db import models
import uuid

# Create your models here.

class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=30)
    employee_email = models.EmailField()
    employee_password= models.CharField(max_length=30)
    employee_age = models.IntegerField()
    employee_image = models.ImageField(upload_to='users/', null=True, blank=True)


    def __str__(self):
        return self.employee_name

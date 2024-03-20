from django.db import models

class Form (models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email=models.EmailField()
    date_from=models.DateField()
    occupation=models.CharField(max_length=80)

    def __str__(self):
        return "Hello this is {} {} .".format(self.first_name,self.last_name)



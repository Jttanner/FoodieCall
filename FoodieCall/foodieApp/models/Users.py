from django.db import models

class Users(models.Model):
    user_UUID = models.UUIDField(primary_key=True, default ='uuid4', editable=False)
    display_name = models.UUIDField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_registered = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

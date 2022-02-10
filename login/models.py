from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
from testdb.models import Test, Utilisateur_Test
# Create your models here.
class MyUser(EmailAbstractUser):
	# Custom fields
	tests = models.ManyToManyField(Test, through='testdb.Utilisateur_Test')
	# Required
	objects = EmailUserManager()
from django.db import models
from django.contrib.auth.models import AbstractUser
from users.querysets.clientqueryset import ClientQueryset
from users.querysets.employeequeryset import EmployeeQueryset



class User(AbstractUser):
    ...


class Client(models.Model):
    birth = models.DateTimeField(blank=True, null=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    objects = ClientQueryset.as_manager()

    def __str__(self) -> str:
        return 'cliend id: #{}'.format(self.id)


class Employee(models.Model):
    birth = models.DateTimeField(blank=True, null=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    objects = EmployeeQueryset.as_manager()

    def __str__(self) -> str:
        return 'employee id: #{}'.format(self.id)
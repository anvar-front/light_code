from statistics import mode
from tabnanny import verbose
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Machine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование станка')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'


class Work(models.Model):
    employee_id = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, verbose_name='Станок', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Начало')
    end_time = models.DateTimeField(verbose_name='Конец')
    salary = models.IntegerField(verbose_name='Зарплата')

    def __str__(self):
        return self.employee_id.name 

    class Meta:
        verbose_name = 'Рабочее время'
        verbose_name_plural = 'Рабочее время'
    
    def save(self):
        if self.employee_id.id == 1 and self.machine_id.id == 1:
            self.salary = self.salary * 6
        elif self.employee_id.id == 2 and self.machine_id.id == 2:
            self.salary = self.salary * 7

        super(Work, self).save()

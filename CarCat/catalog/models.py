from django.db import models
from django.urls import reverse

# Create your models here.

class CarClass(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите класс автомобиля",
                            verbose_name="Класс автомобиля")

    def __str__(self):
        return self.name


class CarUnit(models.Model):
    carmodel = models.CharField(max_length=50,
                                help_text="Введите модель автомобиля",
                                verbose_name="Модель автомобиля")
    carclass = models.ForeignKey('CarClass', on_delete=models.CASCADE,
                                 help_text="Выберите класс автомобиля",
                                 verbose_name="Класс автомобиля", null=True)
    summary = models.TextField(max_length=1000,
                               help_text="Введите краткие сведения об автомобиле")
    winnum =models.CharField(max_length=17,
                             help_text="Должно содержать 17 символов",
                             verbose_name="WIN номер")


    def __str__(self):
        return self.carmodel
    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])

class Status(models.Model):
    name = models.CharField(max_length=20,
                                help_text="Введите статус автомобиля",
                                verbose_name="Статус автомобиля")
    def __str__(self):
        return self.name

class CarInstance(models.Model):
    carunit = models.ForeignKey('CarUnit', on_delete=models.CASCADE, null=True)
    govnum = models.CharField(max_length=9, null=True,
                              help_text="Введите гос номер",
                              verbose_name="Госномер")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text="Изменить статус автомобиля",
                               verbose_name="Статус автомобиля")
    due_back = models.DateField(null=True, blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")

    def __str__(self):
        return '%s %s %s' % (self.govnum, self.carunit, self.status)

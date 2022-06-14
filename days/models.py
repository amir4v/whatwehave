from django.db import models
from django.contrib.auth.models import User


class Year(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class Month(models.Model):
    class NamesOfMonths(models.TextChoices):
        N1 = '1', 'فروردین'
        N2 = '2', 'اردیبهشت'
        N3 = '3', 'خرداد'
        N4 = '4', 'تیر'
        N5 = '5', 'مرداد'
        N6 = '6', 'شهریور'
        N7 = '7', 'مهر'
        N8 = '8', 'آبان'
        N9 = '9', 'آذر'
        N10 = '10', 'دی'
        N11 = '11', 'بهمن'
        N12 = '12', 'اسفند'

    names = {
        '1': 'فروردین',
        '2': 'اردیبهشت',
        '3': 'خرداد',
        '4': 'تیر',
        '5': 'مرداد',
        '6': 'شهریور',
        '7': 'مهر',
        '8': 'آبان',
        '9': 'آذر',
        '10': 'دی',
        '11': 'بهمن',
        '12': 'اسفند',
    }

    month = models.CharField(max_length=2, choices=NamesOfMonths.choices)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def name(self):
        return self.names.get(self.month)

    def __str__(self):
        return self.month


class Day(models.Model):
    class NamesOfDays(models.TextChoices):
        SH = 'ش', 'شنبه'
        YE = 'ی', 'یک شنبه'
        DO = 'د', 'دو شنبه'
        SE = 'س', 'سه شنبه'
        CH = 'چ', 'چهار شنبه'
        PA = 'پ', 'پنج شنبه'
        JO = 'ج', 'جمعه'
    
    names = {
        'ش': 'شنبه',
        'ی': 'یک شنبه',
        'د': 'دو شنبه',
        'س': 'سه شنبه',
        'چ': 'چهار شنبه',
        'پ': 'پنج شنبه',
        'ج': 'جمعه',
    }

    day = models.IntegerField() # 1-6:31 , 7-11:30 , 12:30/(29|30)
    chand_shanbe = models.CharField(max_length=1, choices=NamesOfDays.choices)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def name(self):
        return self.names.get(self.chand_shanbe)

    def __str__(self):
        return str(self.day)


class Note(models.Model):
    note = models.CharField(max_length=500)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note[:10]
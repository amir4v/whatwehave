from proxy import Year, Month, Day


from_year = 1401
to_year = 1401


def build_years():
    for year in range(from_year, to_year+1):
        try:
            Year.objects.create(year=year)
        except:
            pass


def build_months():
    months = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
    ]
    for year in Year.objects.filter(year__gte=from_year, year__lte=to_year).order_by('year'):
        for month in months:
            Month.objects.create(year=year, month=month)


def build_days():
    rozha = [
            'ش',
            'ی',
            'د',
            'س',
            'چ',
            'پ',
            'ج',
        ]
    roz = 3

    for year in range(from_year, to_year+1):
        y = Year.objects.get(year=year)
        months = y.month_set.all()

        month_flag = 1
        for m in months:
            if month_flag <= 6:
                for d in range(1, 31+1):
                    Day.objects.create(month=m, day=d, chand_shanbe=rozha[roz-1])
                    if roz == 7:
                        roz = 1
                    else:
                        roz += 1

            else:
                for d in range(1, 30+1):
                    Day.objects.create(month=m, day=d, chand_shanbe=rozha[roz-1])
                    if roz == 7:
                        roz = 1
                    else:
                        roz += 1
            
            month_flag += 1


def build():
    Year.objects.all().delete()
    Month.objects.all().delete()
    Day.objects.all().delete()

    build_years()
    build_months()
    build_days()


build()

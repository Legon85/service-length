import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.http import HttpResponse


# def index_page(request):
#     return render(request, 'index.html')


def index_page(request):
    coefficient = 1.5
    birthdate = datetime.date(1985, 9, 30)
    today = datetime.datetime.now()

    start_army = datetime.date(2004, 5, 5)  # начальная дата
    end_army = datetime.date(2006, 6, 22)  # конечная дата
    army_period = end_army - start_army  # вычисленный промежуток между датами (выводится в виде timedelta в днях)

    start_fsin = datetime.date(2006, 12, 15)  # начальная дата
    end_fsin = datetime.date(2008, 11, 19)  # конечная дата
    fsin_period = end_fsin - start_fsin
    fsin_pref_period = fsin_period * coefficient

    start_fsb = datetime.date(2008, 11, 20)  # начальная дата
    end_fsb = datetime.datetime.today().date()  # конечная дата
    fsb_period = end_fsb - start_fsb
    fsb_pref_period = fsb_period * coefficient

    age_delta = relativedelta(today, birthdate)
    total_calendar_period = (army_period + fsin_period + fsb_period).days
    total_pref_period = (army_period + fsin_pref_period + fsb_pref_period).days

    data = {
        'age': f'Возраст: {age_delta.years} лет {age_delta.months} месяцев {age_delta.days} дней.',
        'calend_ser': f'Общий календарный стаж: {total_calendar_period // 365} лет {total_calendar_period % 365 // 31} месяцев {total_calendar_period % 365 % 31} дней.',
        'pref_ser': f'Общий льготный стаж: {total_pref_period // 365} лет {total_pref_period % 365 // 31} месяцев {total_pref_period % 365 % 31} дней.'
    }
    return render(request, 'index.html', data)

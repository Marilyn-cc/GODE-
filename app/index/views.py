from datetime import timedelta

from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.shortcuts import render
from django.utils import timezone

from .models import Cow, MilkYield


def home(request):
    today = timezone.localdate()
    yesterday = today - timedelta(days=1)
    start_7 = today - timedelta(days=6)

    total_expr = ExpressionWrapper(F('morning') + F('evening'), output_field=DecimalField())

    today_total = (
        MilkYield.objects.filter(date=today)
        .aggregate(total=Sum(total_expr))['total'] or 0
    )
    yesterday_total = (
        MilkYield.objects.filter(date=yesterday)
        .aggregate(total=Sum(total_expr))['total'] or 0
    )

    # If you don't yet track sales/spillage, treat "accounted" as what you produced.
    # Later: replace accounted_total with sum from MilkSale / inventory usage.
    accounted_total = today_total
    unaccounted = max(today_total - accounted_total, 0)

    # Deficit vs yesterday (only show deficit when today < yesterday)
    deficit = max(yesterday_total - today_total, 0)

    daily_totals = list(
        MilkYield.objects.filter(date__range=(start_7, today))
        .values('date')
        .annotate(total=Sum(total_expr))
        .order_by('date')
    )

    context = {
        'today': today,
        'yesterday': yesterday,

        'today_total': today_total,
        'yesterday_total': yesterday_total,
        'diff_vs_yesterday': today_total - yesterday_total,

        'accounted_total': accounted_total,
        'unaccounted_total': unaccounted,
        'deficit_total': deficit,

        'daily_totals': daily_totals,

        # keep these dummy until you add anomaly model/rules
        'anomaly_count': 3,
    }
    return render(request, 'index/dashboard.html', context)
    
def cows(request):
    return render(request, 'index/cows.html')

def production(request):
    return render(request, 'index/production.html')

def mpesa(request):
    return render(request, 'index/mpesa.html')

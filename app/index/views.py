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

    # Cow counts
    cows_active = Cow.objects.filter(status='active').count()
    cows_dry = Cow.objects.filter(status='dry').count()
    cows_sold = Cow.objects.filter(status='sold').count()

    # Milk totals
    today_total = (
        MilkYield.objects.filter(date=today)
        .aggregate(total=Sum(total_expr))['total'] or 0
    )
    yesterday_total = (
        MilkYield.objects.filter(date=yesterday)
        .aggregate(total=Sum(total_expr))['total'] or 0
    )
    last7_total = (
        MilkYield.objects.filter(date__range=(start_7, today))
        .aggregate(total=Sum(total_expr))['total'] or 0
    )

    # Average per active cow (today)
    avg_per_active_cow = (today_total / cows_active) if cows_active else 0

    # Daily totals for a simple chart/table
    daily_totals = list(
        MilkYield.objects.filter(date__range=(start_7, today))
        .values('date')
        .annotate(total=Sum(total_expr))
        .order_by('date')
    )

    # Top producing cow today (if any)
    top_cow_today = (
        MilkYield.objects.filter(date=today)
        .values('cow__id', 'cow__tag', 'cow__name')
        .annotate(total=Sum(total_expr))
        .order_by('-total')
        .first()
    )

    context = {
        # dates
        'today': today,
        'yesterday': yesterday,
        'start_7': start_7,

        # cows
        'cows_active': cows_active,
        'cows_dry': cows_dry,
        'cows_sold': cows_sold,

        # milk KPIs
        'today_total': today_total,
        'yesterday_total': yesterday_total,
        'last7_total': last7_total,
        'avg_per_active_cow': avg_per_active_cow,
        'top_cow_today': top_cow_today,

        # chart/table data
        'daily_totals': daily_totals,

        # keep placeholders for predictive widgets
        'predicted_next7_total': None,
        'health_risk_alerts': [],
    }
    return render(request, 'index/dashboard.html', context)
    
def cows(request):
    return render(request, 'index/cows.html')

def production(request):
    return render(request, 'index/production.html')

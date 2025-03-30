# Deepseek code, not great.


from django.shortcuts import render
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime, date
import calendar
import json
from .models import Event

@staff_member_required
def event_dashboard(request):
    # Get requested month/year or use current
    now = datetime.now()
    month = int(request.GET.get('month', now.month))
    year = int(request.GET.get('year', now.year))
    
    # Calculate all days in month
    _, last_day = calendar.monthrange(year, month)
    all_days = [date(year, month, day).strftime('%Y-%m-%d') for day in range(1, last_day + 1)]
    
    # Get data for all event types
    events_data = []
    event_names = Event.objects.filter(
        created__year=year,
        created__month=month
    ).values_list('name', flat=True).distinct()
    
    for name in event_names:
        # Initialize with zeros
        daily_counts = {day: 0 for day in all_days}
        # Update with actual counts
        counts = (
            Event.objects.filter(name=name, created__year=year, created__month=month)
            .extra(select={'day': "date(created)"})
            .values('day')
            .annotate(count=Count('id'))
        )
        for entry in counts:
            daily_counts[entry['day']] = entry['count']
        
        events_data.append({
            'name': name,
            'total': Event.objects.filter(name=name, created__year=year, created__month=month).count(),
            'labels': all_days,
            'counts': [daily_counts[day] for day in all_days]
        })
    
    # Pagination controls
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    
    return render(request, 'events/dashboard.html', {
        'events_data_json': json.dumps(events_data),
        'current_month': month,
        'current_year': year,
        'month_name': date(year, month, 1).strftime('%B'),
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'show_prev': not (month == now.month and year == now.year)
    })

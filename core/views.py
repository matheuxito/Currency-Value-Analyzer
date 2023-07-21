from django.shortcuts import render

from datetime import date, timedelta
import plotly.graph_objects as go

def index(request):
    one_year_ago = date.today() - timedelta(days=365)
    current_date = date.today()

    context = {
        'one_year_ago': one_year_ago,
        'current_date': current_date,
    }
    return render(request, 'core/index.html', context)
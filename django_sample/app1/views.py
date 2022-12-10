from django.views.generic import ListView
from .models import TestData


class IndexView(ListView):
    template_name: str = "app1/index.html"
    model = TestData

from django.views.generic import TemplateView

from .models import TestData


class IndexView(TemplateView):
    template_name: str = "app1/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['object_list'] = TestData.objects.all()
        return ctx

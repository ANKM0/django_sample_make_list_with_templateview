from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from .models import TestData


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    model = TestData
    user_info_object_list = model.objects.all()

    def get(self, request, *args, **kwargs):
        object_list = self.user_info_object_list
        context = {
            "object_list": object_list,
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     object_list = self.user_info_object_list
    #     context = {
    #         "object_list": object_list,
    #     }
    #     return render(request, self.template_name, context)
    #     return redirect("app1:index")

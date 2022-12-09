from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
# from django.urls import reverse
from django.shortcuts import render, redirect


# メールテスト用
from django.core.mail import send_mail
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name: str = "app1/index.html"

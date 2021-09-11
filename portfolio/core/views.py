
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutModel.objects.first()
        context['services'] = ServiceModel.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

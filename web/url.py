from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='home'),
    path('hatespeech', TemplateView.as_view(template_name='hatespeech/index.html'), name='hatespeech'),
]
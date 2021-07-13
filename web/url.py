from django.urls import path, include, re_path
from django.views.generic import TemplateView
from web import views as webview

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='home'),
    path('hatespeech/', webview.indexHatespeech, name='hatespeech'),
   # path('hatespeech/syiah/', TemplateView.as_view(template_name='hatespeech/hatespeech.html'), name='syiah'),
    #path('hatespeech/cina/', TemplateView.as_view(template_name='hatespeech/hatespeech.html'), name='cina'),
    #path('hatespeech/ahmadiyah/', TemplateView.as_view(template_name='hatespeech/hatespeech.html'), name='ahmadiyah'),
    #path('hatespeech/hoax/', TemplateView.as_view(template_name='hatespeech/grid.html'), name='hoax'),
]
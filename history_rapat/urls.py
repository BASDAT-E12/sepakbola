from django.urls import path
from history_rapat.views import *
app_name = 'history_rapat'

urlpatterns = [
    path('', show_history_rapat, name='show_history_rapat'),
    path('isi_rapat/<str:id>/', show_isi_rapat, name='show_isi_rapat'),
]
from django.urls import path
from .views import index, detail_menu, detail_submenu

app_name = 'main'

urlpatterns = [
    path('<int:menu_pk>/<int:pk>/', detail_submenu, name='detail_submenu'),
    path('<int:pk>/', detail_menu, name='detail_menu'),
    path('', index, name='index')
]

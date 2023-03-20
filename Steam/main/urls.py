from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games', views.games, name='hry'),
    path('game/<id>', views.game, name='hra'),
    path('publisher/<id>', views.publisher, name='vydavatel'),
    path('add', views.add, name='add'),
    path('update/<id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #goto views file and index function for empty path.
    #e.g. /polls/5/
    path('<int:question_id>/',views.detail, name = 'detail'),
    path('<int:question_id>/results/',views.results, name = 'results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]

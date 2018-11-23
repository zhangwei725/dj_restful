from django.conf.urls import url

from main import views

urlpatterns = [
    url('film/', views.FilmView.as_view())

]

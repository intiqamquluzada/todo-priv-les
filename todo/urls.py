from django.urls import path
from todo.views import *

app_name = "todo"
urlpatterns = [

    path("", index_view, name='index'),
    path("add/", add_view, name='add'),
    path("detail/<int:id>/", detail_view, name="detail"),


]
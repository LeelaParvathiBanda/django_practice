from .views import *
from django.urls import path

urlpatterns = [
    path("add-team/",TableView.as_view(),name="add_team" )
]
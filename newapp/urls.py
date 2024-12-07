from .views import *
from django.urls import path

urlpatterns = [
    path("add-team/",tableView.as_view(),name="add_team")

]
from .views import *
from django.urls import path

urlpatterns = [
    path("add-team/",tableView.as_view(),name="add_team"),
    path("team/list/", ListTablesView.as_view(),name="list_team"),
    path("team/players/<int:id>/", AllPlayersOfTeam.as_view(), name="list_players"),

]
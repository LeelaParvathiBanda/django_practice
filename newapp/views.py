from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *

class tableView(TemplateView):
    template_name = "team.html"
    def post(self, request):# static function is get
        TeamModel.objects.create(t_name=request.POST['teamname'])
        return render(request,self.template_name,locals()) 


class ListTablesView(TemplateView):
    template_name = "teams_list.html"
    def get(self, request):
        teams = TeamModel.objects.all()
        return render(request, self.template_name, locals())


class AllPlayersOfTeam(TemplateView):
    template_name = 'teamPlayers.html'
    def get(self, request, id):
        players = playerModel.objects.filter(ptname=id)
        if players:
            teamname = players.first().ptname.t_name
        else:
            teamname = TeamModel.objects.get(id=id).t_name
        return render(request, self.template_name, locals())
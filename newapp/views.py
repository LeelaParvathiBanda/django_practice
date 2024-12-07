from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
class tableView(TemplateView):
    template_name = "team.html"
    def post(self, request):# static function is get
        TeamModel.objects.create(t_name=request.POST['teamname'])
        return render(request,self.template_name,locals()) 
# Create your views here.

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
# Create your views here.
class TableView(TemplateView):
    template_name = "team.html"
    def post(self, request):
        TeamModel.objects.create(tname = request.POST['teamname'])
        return render(request, self.template_name,locals())
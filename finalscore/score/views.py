from django.shortcuts import render
from .models import Branch, StudentScore
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'base.html')


@method_decorator(login_required, name="dispatch")    
class  Resultlistview(ListView):
    model = StudentScore
    def get_queryset(self):
        if self.request.user.is_superuser:
            return StudentScore.objects.order_by("-id")
        else:
            return StudentScore.objects.filter(branch=self.request.user.profile.branch).order_by("id")
        
    


@method_decorator(login_required, name="dispatch")    
class Resultdetailview(DetailView):
    model = StudentScore
   


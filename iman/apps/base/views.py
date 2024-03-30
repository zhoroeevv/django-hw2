from django.shortcuts import render
from apps.base.models import InfoUser

# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    return render(request, "index.html",locals())



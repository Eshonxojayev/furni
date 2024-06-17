from django.views import View
from .models import Users
from django.shortcuts import render

class UserView(View):
    def get(self, request):
        users = Users.objects.all()
        return render(request, 'users.html', {'users': users})

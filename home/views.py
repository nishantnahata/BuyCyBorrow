from django.shortcuts import render

# Create your views here.
from django.views import View


class HomePage(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
from django.shortcuts import render

from django.views import View

from borrow.models import Cycle


class buyPageView(View):
    template_name = 'cyclelist.html'

    def get(self, request):
        cycles = Cycle.objects.all().filter(is_borrowed=False)
        return render(request, self.template_name, {'cycles': cycles})


class buyView(View):
    template_name = 'buy.html'

    def get (self,request,cid):
        cycle=Cycle.objects.get(pk=cid)
        return render(request,self.template_name,{'cycle':cycle})

    def post (self,request,cid):
        cycle=Cycle.objects.get(pk=cid)
        cycle.set_borrowed()
        return render(request,self.template_name,{'cycle':cycle})

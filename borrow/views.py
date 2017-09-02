from django.shortcuts import render
from django.views import View

from borrow.models import Cycle


class borrowPageView(View):
    template_name = 'borrow_page.html'

    def get(self, request):
        cycles = Cycle.objects.all().filter(is_borrowed=False)
        return render(request, self.template_name, {'cycles': cycles})


class borrowView(View):
    template_name = 'borrow.html'

    def get(self, request, cid):
        cycle = Cycle.objects.get(pk=cid)
        return render(request, self.template_name, {'cycle': cycle})

    def post(self, request, cid):
        cycle = Cycle.objects.get(pk=cid)
        cycle.set_borrowed()
        return render(request,'borrowed.html',{'cycle':cycle})

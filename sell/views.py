from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .modelForms import sellForm

class sellView(View):
    template_name='sell.html'
    form_class=sellForm

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

        cycle = form.save(commit=False)
        return render(request, self.template_name, {'form': form, 'success': True})
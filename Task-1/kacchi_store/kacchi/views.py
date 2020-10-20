from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import kacchi
from .forms import kacchiForm

class kacchiList(ListView): 
    model = kacchi

class kacchiDetail(DetailView): 
    model = kacchi

class kacchiCreate(SuccessMessageMixin, CreateView): 
    model = kacchi
    form_class = kacchiForm
    success_url = reverse_lazy('kacchi_list')
    success_message = "kacchi successfully created!"

class kacchiUpdate(SuccessMessageMixin, UpdateView): 
    model = kacchi
    form_class = kacchiForm
    success_url = reverse_lazy('kacchi_list')
    success_message = "kacchi successfully updated!"

class kacchiDelete(SuccessMessageMixin, DeleteView):
    model = kacchi
    success_url = reverse_lazy('kacchi_list')
    success_message = "kacchi successfully deleted!"

def daily_sell(request):
    queryset = Itemsells.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(date_time__icontains=query) 
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

def sells_create(request):
    submit = False
    if request.method == 'POST':
       
        sells_form = sellsForm(data=request.POST)
        if sells_form.is_valid():

            sells = sells_form.save()

            submit = True
        else:
            print(sells_form.errors)
    else:
        sells_form = sellsForm()
        
    return render(request, 'sells.html',
                  {'sells_form': sells_form,
                   'submit': submit})
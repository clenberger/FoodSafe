from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import FoodForm
from .models import FoodItem
from django.urls import reverse_lazy
from django.template import loader
from django.contrib.auth import logout
from django.contrib import messages





class FoodListView(ListView):
    """ Renders a list of all items. """
    model = FoodItem

    def get(self, request):
        """ GET a list of items. """
        items = self.get_queryset().all()
        return render(request, 'food/index.html', {
            'items': items
        })

class FoodCreateView(CreateView):
    def get(self, request):
        context = {"form": FoodForm()}
        return render(request, 'food/item_form.html', context)
    
    def post(self, request):
        form = FoodForm(request.POST)
        if form.is_valid():
            item = form.save()
            
            return HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'index.html', {'form': form})
    
def delete_item(request,item_id=None):
    item_to_delete=FoodItem.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('index'))

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('food/')
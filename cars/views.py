
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cars.models import Car
from cars.forms import register_car



class ListViewCars(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars

class DetailViewsCar(DetailView):
    model = Car
    template_name = "car_detail.html"

@method_decorator(login_required(login_url='LoginAccounts'), name='dispatch')
class CreateViewCars(CreateView):
    model = Car
    template_name = "new_car.html"
    form_class = register_car
    success_url = reverse_lazy('ListViewCars')  # name da url

@method_decorator(login_required(login_url='LoginAccounts'), name='dispatch')
class UpdateViewCars(UpdateView):
    model = Car
    template_name = "car_update.html"
    form_class = register_car

    def get_success_url(self):
        return reverse_lazy('DetailViewsCar', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='LoginAccounts'), name='dispatch')
class DeleteViewCars(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = reverse_lazy('ListViewCars')  # name da url


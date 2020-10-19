from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(ListView):
    model = Employee
    template_name = 'employee/index.html'


class EmpAddView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/addemp.html'
    success_url = reverse_lazy('index')


class EmpUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/addemp.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Employee, employee_id=id)


class EmpView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee/empview.html'

class EmpDetails(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee/empdetails.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Employee, employee_id=id)

class DeleteEmp(LoginRequiredMixin,DeleteView):
    model = Employee
    template_name = "employee/delete.html"
    success_url = reverse_lazy('index')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Employee, employee_id=id)


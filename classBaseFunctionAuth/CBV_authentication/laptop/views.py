from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class  laptop_view(LoginRequiredMixin,View):
    def get(self,request):
        form=LaptopForm()
        template='laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)
    def post(self,request):
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlaptop')

class laptop_info(View):
    def get(self,request):
        lap_list=Laptop.objects.all()
        template='laptop/showlaptop.html'
        context={'lap_list':lap_list}
        return render(request,template,context)

class Data_update(LoginRequiredMixin,View):
    def get(self,request,id):
        lap_list=Laptop.objects.get(id=id)
        form=LaptopForm(instance=lap_list)
        template='laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)
    def post(self,request,id):
        lap_list=Laptop.objects.get(id=id)
        form=LaptopForm(request.POST,instance=lap_list)
        if form.is_valid():
            form.save()
            return redirect('showlaptop')
        template='laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)

class Delete_data(LoginRequiredMixin,View):
    def get(self,request,id):
        lap_obj=Laptop.objects.get(id=id)
        template='laptop/confirm_for_delete.html'
        context={'lap_obj':lap_obj}
        return render(request,template,context)

    def post(self,request,id):
        lap_obj=Laptop.objects.get(id=id)
        lap_obj.delete()
        lap_obj.save()
        return redirect('showlaptop')

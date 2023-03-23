from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView

from .forms import ClientNewforms,ClientEditforms
from .models import Client
# Create your views here.


class DashboardView(View):

    def get(self, request):
        return render(request, 'billings/dashboard.html',)


class ClientView(View):

    def get(self, request):
        data = Client.objects.all()
        response_data = list(data.values())
        return render(request, 'billings/client/client.html', {'data': response_data})

    def post(self, request):
        pk = request.POST.get("pk")
        Client.objects.get(pk=pk).delete()
        return redirect('clients')

class NewClientView(View):
    def get(self, request):
        form = ClientNewforms
        return render(request, 'billings/client/addclient.html', {'form': form})


    def post(self, request):
        form = ClientNewforms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'billings/client/client.html',)
        else:
            errors = form.errors.as_json()
            return render(request, 'billings/client/addclient.html', {'form': form})

class DetailClientView(View):

    def fetch(self,pk):
        data = Client.objects.get(pk=pk)
        return data

    def get(self, request,pk,):
        data = self.fetch(pk)
        form = ClientEditforms(instance=data)
        return render(request, 'billings/client/editclient.html', {'form': form,'title':data.name})


    def post(self, request,pk):
        form = ClientEditforms(request.POST, instance=self.fetch(pk))

        if form.is_valid():
            form.save()
            return redirect('clients')
        else:
            errors = form.errors.as_json()
            return render(request, 'billings/client/editclient.html', {'form': form})


class DeleteClientView(DeleteView):
    # specify the model you want to use
    model = Client

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "clients"


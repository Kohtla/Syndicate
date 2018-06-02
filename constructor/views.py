from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from .models import Product
#from .serializers import ProductSerializer
from django.views import generic
from django.views.generic import View
from django.shortcuts import render


# Create your views here.

class IndexView(View):
    template_name = 'constructor/index.html'

    # display blank form
    def get(self, request):
        return render(request, self.template_name, None)

    # process from data
    #def post(self, request):

class Constructor(View):
    template_name = 'constructor/Syndicate/Syndicate.html'
    def get(self, request):
        return render(request, self.template_name, None)

    #def post(self,request):
        #somedata = request.POST['sometext']
        #return render_to_response


class Builder(View):
    template_name = 'constructor/Syndicate/Syndicate.html'
    def get(self, request):
        return render(request, self.template_name, None)

    #def post(self,request):
        #somedata = request.POST['sometext']
        #return render_to_response


# Create your views here.

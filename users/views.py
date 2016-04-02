from django.shortcuts import render, HttpResponse
from django.views.generic import View
import json
from rest_framework.views import APIView

# Create your views here.


class Register(View):
    template_name = 'index.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class AddStateCity(View):
    template_name = 'AddStateCity.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class Test(View):
    template_name = 'dashboard.html'

    def get(self, request, tmp_name):
        self.template_name = tmp_name + ".html"
        body = render(request, self.template_name)
        return HttpResponse(body)


class TestPostData(APIView):
    def post(self, request):
        if request.method == 'POST':
            print(json.loads(request.body))
            if 'data' in json.loads(request.body):
                print("yes")
        return HttpResponse()
from django.shortcuts import render, HttpResponse
from django.template.loaders.app_directories import Loader
from django.views.generic import View
import json
from rest_framework.views import APIView
from organization.template_loader import *
# Create your views here.

static = '/static/'


class Home(View):
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
            data = (request.POST.get('jsonData'))
            print(data)
            print (json.loads(data))
            '''
            print(json.loads(request.body))
            if 'data' in json.loads(request.body):
                print("yes")
                '''
        return HttpResponse()


class GetAddCityTemplateSource(APIView):
    template_name = 'index.html'

    def get(self, request, template_name):
        if request.method == 'GET':
            body = None
            if template_name == 'statecity':
                body = render(request, self.template_name, {'view': 'templates/AddStateCity.html'})
            elif template_name == 'statepin':
                body = render(request, self.template_name, {'view': 'templates/AddSubCityPin.html'})
            elif template_name == 'view':
                body = render(request, self.template_name, {'view': 'templates/ViewLocation.html'})
            elif template_name == 'college':
                body = render(request, self.template_name, {'view': 'templates/CollegeMaster.html'})
            elif template_name == 'school':
                body = render(request, self.template_name, {'view': 'templates/ViewLocation.html'})
            elif template_name == 'coaching':
                body = render(request, self.template_name, {'view': 'templates/CollegeMaster.html'})
            elif template_name == 'schoollist':
                body = render(request, self.template_name, {'view': 'templates/SchoolRegister.html'})
            elif template_name == 'collegelist':
                body = render(request, self.template_name, {'view': 'templates/CollegeRegister.html'})
            elif template_name == 'coachinglist':
                body = render(request, self.template_name, {'view': 'templates/CoachingRegister.html'})
            return HttpResponse(body)
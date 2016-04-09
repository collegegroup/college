from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
# Create your views here.


class ReviewHome(APIView):
    template_name = 'ReviewIndex.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class ReviewPage(APIView):
    template_name = 'Review.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)
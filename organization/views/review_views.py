from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..coaching_services import InstituteOrm
from ..school_services import SchoolOrm
from ..college_services import CollegeOrm
from ..dataserializers.school_serializer import SchoolSmallSerializer
from ..dataserializers.coaching_serializer import CoachingSmallSerializer
from ..dataserializers.college_serializer import CollegeSmallSerializer
import json
__author__ = 'ravi'
# Create your views here.


class GetOrganizationDetails(APIView):

    def post(self, request):
        if request.method == "POST":
            institute_list = list()
            school_list = list()
            college_list = list()
            institute_dict = dict()
            school_dict = dict()
            college_dict = dict()
            response = dict()
            name_prefix = request.POST.get('name_prefix')
            try:
                institutes = InstituteOrm.get_institutes_by_name(name_prefix)
                schools = SchoolOrm.get_schools_by_name(name_prefix)
                colleges = CollegeOrm.get_colleges_by_name(name_prefix)
                coaching_serializer = CoachingSmallSerializer(institutes, many=True)
                school_serializer = SchoolSmallSerializer(schools, many=True)
                college_serializer = CollegeSmallSerializer(colleges, many=True)

                for institute in coaching_serializer.data:
                    institute_dict.update({'id': institute['institute_id']})
                    institute_dict.update({'name': institute['institute_name']})
                    institute_dict.update({'type': 'coaching'})
                    institute_list.append(institute_dict)
                for school in school_serializer.data:
                    school_dict.update({'id': school['school_id']})
                    school_dict.update({'name': school['school_name']})
                    school_dict.update({'type': 'school'})
                    school_list.append(school_dict)
                for college in college_serializer.data:
                    college_dict.update({'id': college['college_id']})
                    college_dict.update({'name': college['college_name']})
                    college_dict.update({'type': 'college'})
                    college_list.append(college_dict)
                response.update({'data': {"academies": school_list + college_list + institute_list}})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                print ("error is ", ex)
                response.update({'message': 'could not get data'})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")


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
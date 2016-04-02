from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..college_services import CollegeOrm, CollegeCourseOrm
from ..jsonparser.college_jsons import *
import json
from ..models import CollegeMain
from django.core.files.base import ContentFile
# Create your views here.


class CollegeRegister(APIView):

    def post(self, request):
        if request.method == 'POST':
            college_json_parser = CollegeJsonParser()
            '''
            college_name = request.POST.get('college_name')
            location = request.POST.get('location')
            establishment = request.POST.get('establishment')
            description = request.POST.get('description')
            affiliation = request.POST.get('affiliation')
            website = request.POST.get('website')
            address = request.POST.get('address')
            landline_num = request.POST.get('landline_num')
            mobile_num = request.POST.get('mobile_num')
            emailid = request.POST.get('emailid')
            highest_package = request.POST.get('highest_package')
            average_package = request.POST.get('average_package')

            college_helper = CollegeHelper(college_name, location, establishment, description, affiliation, website,
                                           address, landline_num, mobile_num, emailid, '', highest_package,
                                           average_package)
                                           '''
            college_helper, courses = college_json_parser.college_register_json_parser(request.body)
            college_orm = CollegeOrm()
            response = dict()
            try:
                college_id = college_orm.save_college(college_helper)
                for course in courses:
                    CollegeCourseOrm.save_college_course(course, college_id)
                response.update({'message': 'date saved successfully!'})
            except Exception as ex:
                response.update({'message': ex})

            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCollegeProfile(APIView):

    def post(self, request):
        if request.method == 'POST':
            response = dict()
            college_main = CollegeOrm.get_college_by_id(request.POST.get('id'))
            image_name = "profile_" + str(college_main.college_id) + ".jpg"
            image = ContentFile(request.FILES['image'].read())
            try:
                college_main.profile_image.save(image_name, image)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_name': '/media/' + str(college_main.profile_image)})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


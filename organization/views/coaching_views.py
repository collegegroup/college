from __future__ import print_function
from django.core.files.base import ContentFile
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, status
from ..coaching_services import InstituteOrm, InstituteCourseOrm
from ..jsonparser.coaching_jsons import *
from django.conf import settings
import json, uuid


# Create your views here.


class CoachingRegister(APIView):
    def post(self, request):
        if request.method == 'POST':
            '''
            institute_name = request.POST.get('institute_name')
            director_name = request.POST.get('director_name')
            location = request.POST.get('location')
            establishment = request.POST.get('establishment')
            description = request.POST.get('description')
            affiliation = request.POST.get('affiliation')
            website = request.POST.get('website')
            address = request.POST.get('address')
            landline_num = request.POST.get('landline_num')
            mobile_num = request.POST.get('mobile_num')
            emailid = request.POST.get('emailid')

            institute_helper = InstituteHelper(institute_name, director_name, location, establishment, description,
                                               affiliation, website, address, landline_num, mobile_num, emailid, '')
            '''
            institute_orm = InstituteOrm()
            institute_json_parser = InstituteJsonParser()
            institute_helper, courses = institute_json_parser.institute_register_json_parser(request.body)
            response = dict()
            try:
                institute_id = institute_orm.save_institute(institute_helper)
                for course in courses:
                    InstituteCourseOrm.save_institute_course(course, institute_id)
                response.update({'message': 'date saved successfully!'})
                response.update({'institute_id': institute_id})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})

            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCoachingProfileTmp(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            institute_main = InstituteOrm.get_institute_by_id(request.POST.get('institute_id'))
            image_name = "profile_" + str(institute_main.institute_id) + ".jpg"
            image = ContentFile(request.FILES['image'].read())
            try:
                institute_main.profile_image.save(image_name, image)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_name': '/media/' + str(institute_main.profile_image)})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': ex})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


class UploadCoachingProfile(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            image_name = settings.MEDIA_ROOT + "profiles/college/profile_" + str(uuid.uuid4()) + ".jpg"
            # image = ContentFile(request.FILES['image'].read())
            try:
                # institute_main.profile_image.save(image_name, image)
                handle_uploaded_file(request.FILES['file'], image_name)
                response.update({'message': 'profile picture uploaded successfully!'})
                response.update({'profile_name': "/" + image_name})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'status': 'success'})
            except Exception as ex:
                response.update({'message': str(ex)})
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'status': 'error'})
            return HttpResponse(json.dumps(response), content_type="application/json")


def handle_uploaded_file(file_obj, image_name):
    try:
        destination = open(image_name, 'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()
    except:
        raise

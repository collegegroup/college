"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from users.views import *
from organization.views.school_views import *
from organization.views.college_views import *
from organization.views.coaching_views import *
from organization.views.location_views import *
from organization.views.review_views import *
from organization.views.college_review_views import AddCollegeReview
from organization.views.school_review_views import AddSchoolReview
from organization.views.coaching_review_views import AddCoachingReview

urlpatterns = [
    url(r'^site-admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name="default"),
    url(r'^home/', Home.as_view(), name="home"),
    url(r'^dashboard/', Dashboard.as_view(), name="dashboard"),
    url(r'^addstatecity/', AddStateCity.as_view(), "addstatecity"),

    # INSTITUTE URLS
    url(r'^register/coaching/', CoachingRegister.as_view()),
    url(r'^upload/coaching/', UploadCoachingProfile.as_view()),
    url(r'^category/coaching/', GetAllCoachingCategory.as_view()),
    url(r'^add/category/coaching/', AddCoachingBasicCourses.as_view()),
    url(r'^category/course/coaching/', GetAllBasicCoachingCourses.as_view()),
    url(r'^coaching/(?P<institute_id>.*)/', GetCoachingForReview.as_view()),


    # SCHOOL URLS
    url(r'^register/school/', SchoolRegister.as_view()),
    url(r'^upload/school/', UploadSchoolProfile.as_view()),
    url(r'^school/(?P<school_id>.*)/', GetSchoolForReview.as_view()),

    # COLLEGE URLS
    url(r'^addcity/', AddCity.as_view()),
    url(r'^register/college/', CollegeRegister.as_view()),
    url(r'^upload/college/', UploadCollegeProfile.as_view()),
    url(r'^category/college', GetAllCollegeCategory.as_view()),
    url(r'^add/category/college', AddCollegeBasicCourses.as_view()),
    url(r'^category/course/college/', GetAllBasicCollegeCourses.as_view()),
    url(r'^college/(?P<college_id>.*)/', GetCollegeForReview.as_view()),

    # REVIEW RELATED ALL URL'S
    url(r'^review/home/', ReviewHome.as_view()),
    url(r'^review/review/', ReviewPage.as_view()),
    url(r'^review/search/', GetOrganizationDetails.as_view()),
    url(r'^review/college/', AddCollegeReview.as_view()),
    url(r'^review/school/', AddSchoolReview.as_view()),
    url(r'^review/coaching/', AddCoachingReview.as_view()),

    # LOCATION URLS
    url(r'^allstate/', GetAllState.as_view()),
    url(r'^allcity/', GetAllCity.as_view()),
    url(r'^addcity/', AddCity.as_view()),
    url(r'^addlocation/', AddLocation.as_view()),
    url(r'^alllocation/', GetLocation.as_view()),

    # EXTRA URLS
    url(r'^addstate/', AddState.as_view()),
    url(r'^location/(?P<template_name>.*)/$', GetAddCityTemplateSource.as_view()),
    url(r'^list/(?P<template_name>.*)/$', GetAddCityTemplateSource.as_view()),
    url(r'^view/(?P<template_name>.*)/$', GetAddCityTemplateSource.as_view()),
    url(r'^test/(?P<tmp_name>.*)$', Test.as_view()),
    url(r'^testdata/', TestPostData.as_view()),
    url(r'^testupload/', UploadCoachingProfileTmp.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
]
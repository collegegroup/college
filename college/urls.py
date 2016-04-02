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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Register.as_view()),
    url(r'^dashboard/', Dashboard.as_view()),
    url(r'^addstatecity/', AddStateCity.as_view()),

    # INSTITUTE URLS
    url(r'^register/coaching/', CoachingRegister.as_view()),
    url(r'^upload/coaching/', UploadCoachingProfile.as_view()),

    # SCHOOL URLS
    url(r'^register/school/', SchoolRegister.as_view()),
    url(r'^upload/school/', SchoolRegister.as_view()),

    # COLLEGE URLS

    url(r'^register/college/', CollegeRegister.as_view()),
    url(r'^upload/college/', UploadCollegeProfile.as_view()),

    # EXTRA URLS
    url(r'^addstate/$', AddState.as_view()),
    url(r'^test/(?P<tmp_name>.*)$', Test.as_view()),
    url(r'^testdata/', TestPostData.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
]
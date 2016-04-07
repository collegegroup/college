from models import InstituteMain, InstituteCourses
import datetime


class InstituteOrm(object):

    @staticmethod
    def save_institute(institute_helper):
        institute_main = InstituteMain()
        institute_main.institute_name = institute_helper.institute_name
        institute_main.director_name = institute_helper.director_name
        institute_main.location = institute_helper.location
        institute_main.establishment = institute_helper.establishment
        institute_main.description = institute_helper.description
        institute_main.affiliation = institute_helper.affiliation
        institute_main.website = institute_helper.website
        institute_main.address = institute_helper.address
        institute_main.landline_num = institute_helper.landline_num
        institute_main.mobile_num = institute_helper.mobile_num
        institute_main.emailid = institute_helper.emailid
        institute_main.facilities = institute_helper.facilities
        institute_main.profile_image = institute_helper.profile_image
        institute_main.lastupd_dttm = datetime.datetime.now()

        try:
            institute_main.save()
            return institute_main.institute_id
        except Exception as ex:
            raise ex

    @staticmethod
    def get_institute_by_id(institute_id):
        institute_main = None
        try:
            institute_main = InstituteMain.objects.get(institute_id=institute_id)
            return institute_main
        except Exception as ex:
            raise ex


class InstituteCourseOrm(object):
    @staticmethod
    def save_institute_course(course, institute_id):
        institute_courses = InstituteCourses()
        institute_courses.college_id = institute_id
        institute_courses.course = course.course
        institute_courses.duration = course.duration
        institute_courses.fee = course.fee
        institute_courses.lastupd_dttm = datetime.datetime.now()
        try:
            institute_courses.save()
        except Exception as ex:
            raise ex


class InstituteHelper(object):
    def __init__(self, institute_name, director_name, location, establishment, description, affiliation, website, address,
                 landline_num, mobile_num, emailid, facilities):
        self.institute_name = institute_name
        self.director_name = director_name
        self.location = location
        self.establishment = establishment
        self.description = description
        self.affiliation = affiliation
        self.website = website
        self.address = address
        self.landline_num = landline_num
        self.mobile_num = mobile_num
        self.emailid = emailid
        self.facilities = facilities

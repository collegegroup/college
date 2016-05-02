from models import InstituteMain, CoachingCategory, CoachingFacilities, BasicCoachingCourses, InstituteCourses
import datetime
__author__ = 'ravi'


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

    @staticmethod
    def get_institutes_by_name(institute_name_prefix):
        institutes = None
        try:
            institutes = InstituteMain.objects.filter(institute_name__startswith=institute_name_prefix)
            return institutes
        except Exception as ex:
            raise ex


class FacilitiesORM(object):
    @staticmethod
    def save_facility(coaching_id, facilities_helper):
        coaching_facilities = CoachingFacilities()
        coaching_facilities.coaching_id = coaching_id
        coaching_facilities.facility_name = facilities_helper.facility_name
        coaching_facilities.facility_status = facilities_helper.facility_status
        coaching_facilities.lastupd_dttm = datetime.datetime.now()
        try:
            coaching_facilities.save()
        except:
            raise


class InstituteCourseOrm(object):
    @staticmethod
    def save_institute_course(course, institute_id):
        institute_courses = InstituteCourses()
        institute_courses.institute_id = institute_id
        institute_courses.course = course.course
        institute_courses.category = course.category
        institute_courses.duration = course.duration
        institute_courses.fee = course.fee
        institute_courses.lastupd_dttm = datetime.datetime.now()
        try:
            institute_courses.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_coaching_courses_by_id(institute_id):
        courses = None
        try:
            courses = InstituteCourses.objects.filter(institute_id=institute_id).order_by('course')
        except Exception as ex:
            raise ex
        return courses



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


class CategoryORM(object):
    @staticmethod
    def get_all_coaching_category():
        coaching_category = None
        try:
            coaching_category = CoachingCategory.objects.all().order_by('category_name')
        except Exception as ex:
            raise ex
        return coaching_category

    @staticmethod
    def add_basic_course(category_name, course_name):
        basic_coaching_courses = BasicCoachingCourses()
        basic_coaching_courses.category_name = category_name
        basic_coaching_courses.course_name = course_name
        basic_coaching_courses.lastupd_dttm = datetime.datetime.now()
        try:
            basic_coaching_courses.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_basic_category_and_course():
        coaching_category = None
        try:
            coaching_category = BasicCoachingCourses.objects.all()
        except Exception as ex:
            raise ex
        return coaching_category

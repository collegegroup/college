from models import CollegeMain, CollegeFacilities, CollegeCourses, CollegeCategory, BasicCollegeCourses
import datetime
__author__ = 'ravi'


class CollegeOrm(object):

    @staticmethod
    def save_college(college_helper):
        college_main = CollegeMain()
        college_main.college_name = college_helper.school_name
        college_main.location = college_helper.location
        college_main.establishment = college_helper.establishment
        college_main.description = college_helper.description
        college_main.affiliation = college_helper.affiliation
        college_main.website = college_helper.website
        college_main.address = college_helper.address
        college_main.landline_num = college_helper.landline_num
        college_main.mobile_num = college_helper.mobile_num
        college_main.emailid = college_helper.emailid
        college_main.profile_image = college_helper.profile_image
        college_main.highest_package = college_helper.highest_package
        college_main.average_package = college_helper.average_package
        college_main.lastupd_dttm = datetime.datetime.now()

        try:
            college_main.save()
            return college_main.college_id
        except:
            raise

    @staticmethod
    def get_college_by_id(college_id):
        college_main = None
        try:
            college_main = CollegeMain.objects.get(college_id=college_id)
            return college_main
        except Exception as ex:
            raise

    @staticmethod
    def get_colleges_by_name(college_name_prefix):
        colleges = None
        try:
            colleges = CollegeMain.objects.filter(college_name__startswith=college_name_prefix)
            return colleges
        except Exception as ex:
            raise ex


class CollegeCourseOrm(object):
    @staticmethod
    def save_college_course(course, college_id):
        college_courses = CollegeCourses()
        college_courses.college_id = college_id
        college_courses.course = course.course
        college_courses.category = course.category
        college_courses.duration = course.duration
        college_courses.fee = course.fee
        college_courses.entrance = course.entrance
        college_courses.lastupd_dttm = datetime.datetime.now()
        try:
            college_courses.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_college_courses_by_id(college_id):
        courses = None
        try:
            courses = CollegeCourses.objects.filter(college_id=college_id).order_by('course')
        except Exception as ex:
            raise ex
        return courses


class FacilitiesORM(object):
    @staticmethod
    def save_facility(college_id, facilities_helper):
        college_facilities = CollegeFacilities()
        college_facilities.college_id = college_id
        college_facilities.facility_name = facilities_helper.facility_name
        college_facilities.facility_status = facilities_helper.facility_status
        college_facilities.lastupd_dttm = datetime.datetime.now()
        try:
            college_facilities.save()
        except:
            raise


class CategoryORM(object):
    @staticmethod
    def get_all_college_category():
        college_category = None
        try:
            college_category = CollegeCategory.objects.all().order_by('category_name')
        except Exception as ex:
            raise ex
        return college_category

    @staticmethod
    def add_basic_course(category_name, course_name):
        basic_college_courses = BasicCollegeCourses()
        basic_college_courses.category_name = category_name
        basic_college_courses.course_name = course_name
        basic_college_courses.lastupd_dttm = datetime.datetime.now()
        try:
            basic_college_courses.save()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_basic_category_and_course():
        college_category = None
        try:
            college_category = BasicCollegeCourses.objects.all()
        except Exception as ex:
            raise ex
        return college_category

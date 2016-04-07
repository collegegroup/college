from models import CollegeMain, CollegeCourses
import datetime


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
        college_main.facilities = college_helper.facilities
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


class CollegeCourseOrm(object):
    @staticmethod
    def save_college_course(course, college_id):
        college_courses = CollegeCourses()
        college_courses.college_id = college_id
        college_courses.course = course.course
        college_courses.duration = course.duration
        college_courses.fee = course.fee
        college_courses.entrance = course.entrance
        college_courses.lastupd_dttm = datetime.datetime.now()
        try:
            college_courses.save()
        except Exception as ex:
            raise ex

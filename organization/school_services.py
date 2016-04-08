from .models import SchoolMain, SchoolFacilities, SchoolCurriculum
import datetime


class SchoolOrm(object):

    @staticmethod
    def save_school(school_helper):
        school_main = SchoolMain()
        school_main.school_name = school_helper.school_name
        school_main.location = school_helper.location
        school_main.establishment = school_helper.establishment
        school_main.description = school_helper.description
        school_main.affiliation = school_helper.affiliation
        school_main.website = school_helper.website
        school_main.school_start_time = school_helper.school_start_time
        school_main.school_end_time = school_helper.school_end_time
        school_main.address = school_helper.address
        school_main.landline_num = school_helper.landline_num
        school_main.mobile_num = school_helper.mobile_num
        school_main.emailid = school_helper.emailid
        school_main.profile_image = school_helper.profile_image
        school_main.lastupd_dttm = datetime.datetime.now()

        try:
            school_main.save()
            return school_main.school_id
        except:
            raise

    @staticmethod
    def get_school_by_id(school_id):
        college_main = None
        try:
            school_main = SchoolMain.objects.get(school_id=school_id)
            return school_main
        except Exception as ex:
            raise


class FacilitiesORM(object):
    @staticmethod
    def save_facility(school_id, facilities_helper):
        school_facilities = SchoolFacilities()
        school_facilities.school_id = school_id
        school_facilities.facility_name = facilities_helper.facility_name
        school_facilities.facility_status = facilities_helper.facility_status
        school_facilities.lastupd_dttm = datetime.datetime.now()
        try:
            school_facilities.save()
        except:
            raise


class CurriculumORM(object):
    @staticmethod
    def save_curriculum(school_id, curriculum_helper):
        school_curriculum = SchoolCurriculum()
        school_curriculum.school_id = school_id
        school_curriculum.curriculum_name = curriculum_helper.curriculum_name
        school_curriculum.curriculum_status = curriculum_helper.curriculum_status
        school_curriculum.lastupd_dttm = datetime.datetime.now()
        try:
            school_curriculum.save()
        except:
            raise
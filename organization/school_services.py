from .models import SchoolMain
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
        school_main.facilities = school_helper.facilities
        school_main.profile_image = school_helper.profile_image
        school_main.extra_curriculum = school_helper.extra_curriculum
        school_main.lastupd_dttm = datetime.datetime.now()

        try:
            school_main.save()
        except:
            raise

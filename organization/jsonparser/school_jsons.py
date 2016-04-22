from __future__ import print_function
import json
__author__ = 'ravi'


class SchoolHelper(object):
    def __init__(self, school_name, location, establishment, description, affiliation, website, school_start_time,
                 school_end_time, address, landline_num, mobile_num, emailid, profile_image):
        self.school_name = school_name
        self.location = location
        self.establishment = establishment
        self.description = description
        self.affiliation = affiliation
        self.website = website
        self.school_start_time = school_start_time
        self.school_end_time = school_end_time
        self.address = address
        self.landline_num = landline_num
        self.mobile_num = mobile_num
        self.emailid = emailid
        self.profile_image = profile_image


class FacilitiesHelper(object):
    def __init__(self, facility_name, facility_status):
        self.facility_name = facility_name
        self.facility_status = facility_status


class CurriculumHelper(object):
    def __init__(self, curriculum_name, curriculum_status):
        self.curriculum_name = curriculum_name
        self.curriculum_status = curriculum_status


class SchoolJsonParser(object):
    def is_not_used(self):
        pass

    def school_register_json_parser(self, json_string):
        self.is_not_used()
        result = dict()
        result = json.loads(json_string)
        school_name = None
        location = None
        establishment = None
        description = None
        affiliation = None
        website = None
        school_start_time = None
        school_end_time = None
        address = None
        landline_num = None
        mobile_num = None
        emailid = None
        profile_image = None
        facilities = list()
        facility_name = None
        facility_status = None
        extra_curriculum = list()
        curriculum_name = None
        curriculum_status = None

        if 'data' in result:
            data = result['data']
            if 'school_name' in result['data']:
                school_name = result['data']['school_name']
            if 'location' in data:
                location = result['data']['location']
            if 'establishment' in data:
                establishment = result['data']['establishment']
            if 'description' in data:
                description = result['data']['description']
            if 'affiliation' in data:
                affiliation = result['data']['affiliation']
            if 'website' in data:
                website = result['data']['website']
            if 'school_start_time' in data:
                school_start_time = result['data']['school_start_time']
            if 'school_end_time' in data:
                school_end_time = result['data']['school_end_time']
            if 'address' in data:
                address = result['data']['address']
            if 'landline_num' in result['data']:
                landline_num = result['data']['landline_num']
            if 'mobile_num' in result['data']:
                mobile_num = result['data']['mobile_num']
            if 'emailid' in result['data']:
                emailid = result['data']['emailid']
            if 'profile_image' in result['data']:
                profile_image = result['data']['profile_image']
            if 'facilities' in result['data']:
                for facility in result['data']['facilities']:
                    if 'text' in facility:
                        facility_name = facility['text']
                    if 'value' in facility:
                        facility_status = facility['value']
                    facilities.append(FacilitiesHelper(facility_name, facility_status))
            if 'extra_curriculum' in result['data']:
                for curriculum in result['data']['extra_curriculum']:
                    if 'text' in curriculum:
                        curriculum_name = curriculum['text']
                    if 'value' in curriculum:
                        curriculum_status = curriculum['value']
                    extra_curriculum.append(CurriculumHelper(curriculum_name, curriculum_status))
        return [SchoolHelper(school_name, location, establishment, description, affiliation, website, school_start_time,
                             school_end_time, address, landline_num, mobile_num, emailid, profile_image),
                facilities, extra_curriculum]

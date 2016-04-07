from __future__ import print_function
import json


class SchoolHelper(object):
    def __init__(self, school_name, location, establishment, description, affiliation, website, school_start_time,
                 school_end_time, address, landline_num, mobile_num, emailid, profile_image,facilities,
                 extra_curriculum):
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
        self.facilities = facilities
        self.profile_image = profile_image
        self.extra_curriculum = extra_curriculum


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
        facilities = None
        profile_image = None
        extra_curriculum = None

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
                facilities = result['data']['profile_image']
            if 'facilities' in result['data']:
                facilities = result['data']['facilities']
            if 'extra_curriculum' in result['data']:
                extra_curriculum = result['data']['extra_curriculum']
        return SchoolHelper(school_name, location, establishment, description, affiliation, website, school_start_time,
                            school_end_time, address, landline_num, mobile_num, emailid, profile_image,
                            facilities, extra_curriculum)

import json
__author__ = 'ravi'


class InstituteHelper(object):
    def __init__(self, institute_name, director_name, location, establishment, description, affiliation, website,
                 address, landline_num, mobile_num, emailid, profile_image):
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
        self.profile_image = profile_image


class InstituteCourseHelper(object):
    def __init__(self, course, category, duration, fee):
        self.course = course
        self.category = category
        self.duration = duration
        self.fee = fee


class FacilitiesHelper(object):
    def __init__(self, facility_name, facility_status):
        self.facility_name = facility_name
        self.facility_status = facility_status


class InstituteJsonParser(object):

    def is_not_used(self):
        pass

    def institute_register_json_parser(self, json_string):
        self.is_not_used()
        result = dict()
        result = json.loads(json_string)
        institute_name = None
        location = None
        establishment = None
        description = None
        affiliation = None
        website = None
        address = None
        landline_num = None
        mobile_num = None
        emailid = None
        facilities = list()
        facility_name = None
        facility_status = None
        director_name = None
        courses = list()
        course_name = None
        category = None
        duration = None
        fee = None
        profile_image = None
        if 'data' in result:
            data = result['data']
            if 'institute_name' in result['data']:
                institute_name = result['data']['institute_name']
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
            if 'address' in data:
                address = result['data']['address']
            if 'landline_num' in result['data']:
                landline_num = result['data']['landline_num']
            if 'mobile_num' in result['data']:
                mobile_num = result['data']['mobile_num']
            if 'emailid' in result['data']:
                emailid = result['data']['emailid']
            if 'facilities' in result['data']:
                for facility in result['data']['facilities']:
                    if 'text' in facility:
                        facility_name = facility['text']
                    if 'value' in facility:
                        facility_status = facility['value']
                    facilities.append(FacilitiesHelper(facility_name, facility_status))
            if 'director_name' in result['data']:
                director_name = result['data']['director_name']
            if 'profile_image' in result['data']:
                profile_image = result['data']['profile_image']
            if 'courses' in result['data']:
                for course in result['data']['courses']:
                    if 'course' in course:
                        course_name = course['course']
                    if 'category' in course:
                        category = course['category']
                    if 'duration' in course:
                        duration = course['duration']
                    if 'fee' in course:
                        fee = course['fee']
                    courses.append(InstituteCourseHelper(course_name, category, duration, fee))
        return [InstituteHelper(institute_name, director_name, location, establishment, description, affiliation,
                                website, address,landline_num, mobile_num, emailid, profile_image), courses, facilities]

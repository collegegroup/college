import json
__author__ = 'ravi'


class CollegeReviewHelper(object):
    def __init__(self, user_id, institute_id, institute_name, course, year_of_batch, fee, review,
                 faculties, administration, alumni, atmosphere):
        self.user_id = user_id
        self.institute_id = institute_id
        self.institute_name = institute_name
        self.course = course
        self.year_of_batch = year_of_batch
        self.fee = fee
        self.review = review
        self.faculties = faculties
        self.administration = administration
        self.alumni = alumni
        self.atmosphere = atmosphere


class CoachingReviewJsonParser(object):

    @staticmethod
    def coaching_review_json_parser(json_string):
        result = json.loads(json_string)
        user_id = None
        institute_id = None
        institute_name = None
        course = None
        year_of_batch = None
        fee = None
        review = None
        faculties = None
        administration = None
        alumni = None
        atmosphere = None

        if 'user_id' in result:
            user_id = result['user_id']
        if 'institute_id' in result:
            institute_id = result['institute_id']
        if 'institute_name' in result:
            institute_name = result['institute_name']
        if 'course' in result:
            course = result['course']
        if 'year_of_batch' in result:
            year_of_batch = result['year_of_batch']
        if 'fee' in result:
            fee = result['fee']
        if 'review' in result:
            review = result['review']
        if 'faculties' in result:
            faculties = result['faculties']
        if 'administration' in result:
            administration = result['administration']
        if 'alumni' in result:
            alumni = result['alumni']
        if 'atmosphere' in result:
            atmosphere = result['atmosphere']
        return CollegeReviewHelper(user_id, institute_id, institute_name, course, year_of_batch, fee, review, faculties,
                                   administration, alumni, atmosphere)

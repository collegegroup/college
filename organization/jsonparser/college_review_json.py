import json


class CollegeReviewHelper(object):
    def __init__(self, user_id, college_id, college_name, course, entrance, rank, passout_year, fee, review, faculties,
                 infrastructure, accommodation, placement, social_life):
        self.user_id = user_id
        self.college_id = college_id
        self.college_name = college_name
        self.course = course
        self.entrance = entrance
        self.rank = rank
        self.passout_year = passout_year
        self.fee = fee
        self.review = review
        self.faculties = faculties
        self.infrastructure = infrastructure
        self.accommodation = accommodation
        self.placement = placement
        self.social_life = social_life


class CollegeReviewJsonParser(object):

    @staticmethod
    def college_review_json_parser(json_string):
        result = json.loads(json_string)
        user_id = None
        college_id = None
        college_name = None
        course = None
        entrance = None
        rank = None
        passout_year = None
        fee = None
        review = None
        faculties = None
        infrastructure = None
        accommodation = None
        placement = None
        social_life = None

        if 'user_id' in result:
            user_id = result['user_id']
        if 'college_id' in result:
            college_id = result['college_id']
        if 'college_name' in result:
            college_name = result['college_name']
        if 'course' in result:
            course = result['course']
        if 'entrance' in result:
            entrance = result['entrance']
        if 'rank' in result:
            rank = result['rank']
        if 'passout_year' in result:
            passout_year = result['passout_year']
        if 'fee' in result:
            fee = result['fee']
        if 'review' in result:
            review = result['review']
        if 'faculties' in result:
            faculties = result['faculties']
        if 'infrastructure' in result:
            infrastructure = result['infrastructure']
        if 'accommodation' in result:
            accommodation = result['accommodation']
        if 'placement' in result:
            placement = result['placement']
        if 'social_life' in result:
            social_life = result['social_life']

        return CollegeReviewHelper(user_id, college_id, college_name, course, entrance, rank, passout_year, fee,
                                   review, faculties, infrastructure, accommodation, placement, social_life)

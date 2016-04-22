import json
__author__ = 'ravi'


class SchoolReviewHelper(object):
    def __init__(self, user_id, school_id, school_name, state_name, class_field, stream, year, board, fee, review,
                 faculties, facilities, infrastructure, extra_curriculum):
        self.user_id = user_id
        self.school_id = school_id
        self.school_name = school_name
        self.state_name = state_name
        self.class_field = class_field
        self.stream = stream
        self.year = year
        self.board = board
        self.fee = fee
        self.review = review
        self.faculties = faculties
        self.facilities = facilities
        self.infrastructure = infrastructure
        self.extra_curriculum = extra_curriculum


class SchoolReviewJsonParser(object):

    @staticmethod
    def school_review_json_parser(json_string):
        result = json.loads(json_string)
        user_id = None
        school_id = None
        school_name = None
        state_name = None
        class_field = None
        stream = None
        year = None
        board = None
        fee = None
        review = None
        faculties = None
        infrastructure = None
        extra_curriculum = None
        facilities = None

        if 'user_id' in result:
            user_id = result['user_id']
        if 'school_id' in result:
            school_id = result['school_id']
        if 'school_name' in result:
            school_name = result['school_name']
        if 'state_name' in result:
            state_name = result['state_name']
        if 'class' in result:
            class_field = result['class']
        if 'stream' in result:
            stream = result['stream']
        if 'board' in result:
            board = result['board']
        if 'year' in result:
            year = result['year']
        if 'fee' in result:
            fee = result['fee']
        if 'review' in result:
            review = result['review']
        if 'faculties' in result:
            faculties = result['faculties']
        if 'infrastructure' in result:
            infrastructure = result['infrastructure']
        if 'facilities' in result:
            facilities = result['facilities']
        if 'extra_curriculum' in result:
            extra_curriculum = result['extra_curriculum']
        return SchoolReviewHelper(user_id, school_id, school_name, state_name, class_field, stream, year, board,
                                  fee, review, faculties, facilities, infrastructure, extra_curriculum)
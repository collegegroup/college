from models import SchoolReview
import datetime
__author__ = 'ravi'


class SchoolReviewORM(object):
    @staticmethod
    def save_school_review(school_review_helper):
        school_review = SchoolReview()
        school_review.user_id = school_review_helper.user_id
        school_review.school_id = school_review_helper.school_id
        school_review.school_name = school_review_helper.school_name
        school_review.state_name = school_review_helper.state_name
        school_review.class_field = school_review_helper.class_field
        school_review.stream = school_review_helper.stream
        school_review.year = school_review_helper.year
        school_review.board = school_review_helper.board
        school_review.fee = school_review_helper.fee
        school_review.review = school_review_helper.review
        school_review.faculties = school_review_helper.faculties
        school_review.facilities = school_review_helper.facilities
        school_review.infrastructure = school_review_helper.infrastructure
        school_review.extra_curriculum = school_review_helper.extra_curriculum
        school_review.lastupd_dttm = datetime.datetime.now()

        try:
            school_review.save()
        except Exception as ex:
            raise ex

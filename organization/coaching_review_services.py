from models import CoachingReview
import datetime
__author__ = 'ravi'


class CoachingReviewORM(object):
    @staticmethod
    def save_coaching_review(coaching_review_helper):
        coaching_review = CoachingReview()
        coaching_review.user_id = coaching_review_helper.user_id
        coaching_review.institute_id = coaching_review_helper.institute_id
        coaching_review.institute_name = coaching_review_helper.institute_name
        coaching_review.course = coaching_review_helper.course
        coaching_review.fee = coaching_review_helper.fee
        coaching_review.year_of_batch = coaching_review_helper.year_of_batch
        coaching_review.review = coaching_review_helper.review
        coaching_review.faculties = coaching_review_helper.faculties
        coaching_review.administration = coaching_review_helper.administration
        coaching_review.alumni = coaching_review_helper.alumni
        coaching_review.atmosphere = coaching_review_helper.atmosphere
        coaching_review.lastupd_dttm = datetime.datetime.now()

        try:
            coaching_review.save()
        except Exception as ex:
            raise ex

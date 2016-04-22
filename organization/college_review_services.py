from models import CollegeReview
import datetime
__author__ = 'ravi'


class CollegeReviewORM(object):
    @staticmethod
    def save_college_review(college_review_helper):
        college_review = CollegeReview()
        college_review.user_id = college_review_helper.user_id
        college_review.college_id = college_review_helper.college_id
        college_review.college_name = college_review_helper.college_name
        college_review.entrance = college_review_helper.entrance
        college_review.course = college_review_helper.course
        college_review.rank = college_review_helper.rank
        college_review.passout_year = college_review_helper.passout_year
        college_review.fee = college_review_helper.fee
        college_review.review = college_review_helper.review
        college_review.faculties = college_review_helper.faculties
        college_review.accommodation = college_review_helper.accommodation
        college_review.infrastructure = college_review_helper.infrastructure
        college_review.placement = college_review_helper.placement
        college_review.social_life = college_review_helper.social_life
        college_review.lastupd_dttm = datetime.datetime.now()
        try:
            college_review.save()
        except Exception as ex:
            raise ex
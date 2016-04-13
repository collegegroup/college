from models import CollegeReview


class CollegeReviewORM(object):
    @staticmethod
    def save_college_review(college_review_helper):
        college_review = CollegeReview()
        college_review.user_id = college_review_helper.user_id
        college_review.college_id = college_review_helper.college_id
        college_review.college_name = college_review_helper.college_name

        try:
            college_review.save()
        except Exception as ex:
            raise ex
/**
 * Created by bhanu on 26/4/16.
 */

var instituteReviewApp = angular.module('mainCollegeApp.instituteReview', []);

instituteReviewApp.controller('instituteReviewCtrl', function($scope, HTTPService, utilityService, $stateParams) {

    $scope.coachingID = $stateParams.acadamyID;

    $scope.coachingJSONData = {

        user_id: "",

        institute_id: $scope.coachingID,

        institute_name: "",

        state_name: "",

        course: "",

        year_of_batch: "",

        fee: "",

        review: "",

        faculties: 1,

        administration: 1,

        alumni: 1,

        atmosphere: 1
    };








    $scope.instituteNameError = false;
    $scope.coursesError = false;
    $scope.yearOfBatchError = false;
    $scope.instituteFeeError = false;
    $scope.instituteFeeFocus = false;
    
    $scope.yearOfBatchFocus = false;
    $scope.coursesFocus = false;
    $scope.instituteNameFocus = false;










    /*
     * This method is used to prepare institute json data
     * */
    $scope.prepareInstituteJSONData = function (jsonData) {

        $scope.coachingJSONData.faculties = jsonData.faculties.toString();
        $scope.coachingJSONData.administration = jsonData.administration.toString();
        $scope.coachingJSONData.alumni = jsonData.alumni.toString();
        $scope.coachingJSONData.atmosphere = jsonData.atmosphere.toString();

        return $scope.coachingJSONData;

    };
    /*
     * This method is used to prepare institute json data
     * */
    
    
    






    /*
     * These are the validation methods for school JSON
     * */
    $scope.validateInstituteName = function (instituteName) {

        if(utilityService.validateText(instituteName, "INSTITUTE REVIEW INSTITUTE NAME VALIDATION")) {

            $scope.instituteNameError = false;
            $scope.instituteNameFocus = false;

            return true;

        }  else {

            $scope.instituteNameError = true;
            $scope.instituteNameFocus = true;

            return false;

        }

    };

    $scope.validateCourses = function (courses) {

        if(utilityService.validateText(courses, "INSTITUTE REVIEW COURSES VALIDATION")) {

            $scope.coursesError = false;
            $scope.coursesFocus = false;

            return true;

        }  else {

            $scope.coursesError = true;
            $scope.coursesFocus = true;

            return false;

        }

    };

    $scope.validateYearOfBatch = function (yearOfBatch) {

        if(utilityService.validateText(yearOfBatch, "INSTITUTE YEAR OF BATCH VALIDATION")) {

            $scope.yearOfBatchError = false;
            $scope.yearOfBatchFocus = false;

            return true;

        }  else {

            $scope.yearOfBatchError = true;
            $scope.yearOfBatchFocus = true;

            return false;

        }

    };

    $scope.validateInstituteFee = function (fee) {

        if(utilityService.validateText(fee, "INSTITUTE FEE VALIDATION")) {

            $scope.instituteFeeError = false;
            $scope.instituteFeeFocus = false;

            return true;

        }  else {

            $scope.instituteFeeError = true;
            $scope.instituteFeeFocus = true;

            return false;

        }

    };
    /*
     * These are the validation methods for school JSON
     * */











    /*
     * This method is used to validate the JSON data
     * */
    $scope.validateInstituteJSONData = function (jsonData) {

        if($scope.validateInstituteName(jsonData.institute_name) &&
            $scope.validateCourses(jsonData.course) &&
            $scope.validateYearOfBatch(jsonData.year_of_batch) &&
            $scope.validateInstituteFee(jsonData.fee)) {

            jsonData = $scope.prepareInstituteJSONData(jsonData);

            return true;

        } else {

            return false;

        }

    };
    /*
     * This method is used to validate the JSON data
     * */









    /*
     * THis is used get particular  coaching record
     * */
    HTTPService.GETRequest('/coaching/'+$scope.coachingID+'/', '', 'getCoachingRecord');
    /*
     * THis is used get particular  coaching record
     * */








    /*
     * This method is used to submit school review
     * */
    $scope.submitCoachingReview = function (coachingJSONData) {

        if($scope.validateInstituteJSONData(coachingJSONData)) {

            var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(coachingJSONData))});

            HTTPService.POSTRequest('/review/coaching/', formData, 'coachingReview');

        }



    };
    /*
     * This method is used to submit school review
     * */









    /*
     * This is for submit coaching review response
     * */
    $scope.$on('coachingReviewSuccess', function (event, response) {

        console.log('Response: ', response);

    });
    $scope.$on('coachingReviewError', function (event, response) {

    });
    /*
     * This is for submit coaching review response
     * */








    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getCoachingRecordSuccess', function (event, response) {

        $scope.coachingJSONData.institute_name = response.data.data.institute_name;

    });
    $scope.$on('getCoachingRecordError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});
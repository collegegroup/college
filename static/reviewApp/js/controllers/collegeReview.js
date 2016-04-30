/**
 * Created by bhanu on 26/4/16.
 */

var collegeReviewApp = angular.module('mainCollegeApp.collegeReview', ['starRating']);

collegeReviewApp.controller('collegeReviewCtrl', function($scope, HTTPService, utilityService, $stateParams) {

    $scope.collegeID = $stateParams.acadamyID;

    $scope.collegeJSONData = {

        user_id: "",

        college_id: $scope.collegeID,

        college_name: "",

        state_name: "",

        course: "",

        entrance:"",

        rank: "",

        pass_out_year: "",

        fee: "",

        review: "",

        accommodation: 1,

        infrastructure: 1,

        faculties: 1,

        placement: 1,

        social_life: 1
    };










    $scope.collegeNameError = false;
    $scope.courseError = false;
    $scope.entranceError = false;
    $scope.rankError = false;
    $scope.passOutYearError = false;
    $scope.collegeFeeError = false;
    
    $scope.collegeFeeFocus = false;
    $scope.passOutYearFocus = false;
    $scope.rankFocus= false;
    $scope.entranceFocus = false;
    $scope.courseFocus = false;
    $scope.collegeNameFocus = false;










    /*
     * This method is used to prepare college json data
     * */
    $scope.prepareCollegeJSONData = function (jsonData) {

        $scope.collegeJSONData.accommodation = jsonData.accommodation.toString();
        $scope.collegeJSONData.infrastructure = jsonData.infrastructure.toString();
        $scope.collegeJSONData.faculties = jsonData.faculties.toString();
        $scope.collegeJSONData.placement = jsonData.placement.toString();
        $scope.collegeJSONData.social_life = jsonData.social_life.toString();

        return $scope.collegeJSONData;

    };
    /*
     * This method is used to prepare college json data
     * */









    /*
     * These are the validation methods for school JSON
     * */
    $scope.validateCollegeName = function (collegeName) {

        if(utilityService.validateText(collegeName, "COLLEGE REVIEW COLLEGE NAME VALIDATION")) {

            $scope.collegeNameError = false;
            $scope.collegeNameFocus = false;

            return true;

        }  else {

            $scope.collegeNameError = true;
            $scope.collegeNameFocus = true;

            return false;

        }

    };

    $scope.validateCourse = function (course) {

        if(utilityService.validateText(course, "COLLEGE REVIEW COURSE VALIDATION")) {

            $scope.courseError = false;
            $scope.courseFocus = false;

            return true;

        }  else {

            $scope.courseError = true;
            $scope.courseFocus = true;

            return false;

        }

    };

    $scope.validateEntrance = function (entrance) {

        if(utilityService.validateText(entrance, "COLLEGE REVIEW ENTRANCE VALIDATION")) {

            $scope.entranceError = false;
            $scope.entranceFocus = false;

            return true;

        }  else {

            $scope.entranceError = true;
            $scope.entranceFocus = true;

            return false;

        }

    };

    $scope.validateRank = function (rank) {

        if(utilityService.validateText(rank, "COLLEGE RANK VALIDATION")) {

            $scope.rankError = false;
            $scope.rankFocus= false;

            return true;

        }  else {

            $scope.rankError = true;
            $scope.rankFocus = true;

            return false;

        }

    };

    $scope.validatePassOutYear = function (passOutYear) {

        if(utilityService.validateText(passOutYear, "SCHOOL BOARD VALIDATION")) {

            $scope.passOutYearError = false;
            $scope.passOutYearFocus = false;

            return true;

        }  else {

            $scope.passOutYearError = true;
            $scope.passOutYearFocus = true;

            return false;

        }

    };

    $scope.validateFee = function (fee) {

        if(utilityService.validateText(fee, "COLLEGE FEE VALIDATION")) {

            $scope.collegeFeeError = false;
            $scope.collegeFeeFocus = false;

            return true;

        }  else {

            $scope.collegeFeeError = true;
            $scope.collegeFeeFocus = true;

            return false;

        }

    };
    /*
     * These are the validation methods for school JSON
     * */

    
    
    
    




    /*
     * This method is used to validate the JSON data
     * */
    $scope.validateCollegeJSONData = function (jsonData) {

        if($scope.validateCollegeName(jsonData.college_name) &&
            $scope.validateCourse(jsonData.course) &&
            $scope.validateEntrance(jsonData.entrance) &&
            $scope.validateRank(jsonData.rank) &&
            $scope.validatePassOutYear(jsonData.pass_out_year) &&
            $scope.validateFee(jsonData.fee)) {

            jsonData = $scope.prepareCollegeJSONData(jsonData);

            return true;

        } else {

            return false;

        }

    };
    /*
     * This method is used to validate the JSON data
     * */









    /*
     * THis is used get particular  college record
     * */
    HTTPService.GETRequest('/college/'+$scope.collegeID+'/', '', 'getCollegeRecord');
    /*
     * THis is used get particular  college record
     * */








    /*
     * This method is used to submit school review
     * */
    $scope.submitCollegeReview = function (collegeJSONData) {

        if($scope.validateCollegeJSONData(collegeJSONData)) {

            var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(collegeJSONData))});

            HTTPService.POSTRequest('/review/college/', formData, 'collegeReview');

        }

    };
    /*
     * This method is used to submit school review
     * */









    /*
     * This is for submit review response
     * */
    $scope.$on('collegeReviewSuccess', function (event, response) {

        

    });
    $scope.$on('collegeReviewError', function (event, response) {

    });
    /*
     * This is for submit review response
     * */








    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getCollegeRecordSuccess', function (event, response) {

        $scope.collegeJSONData.college_name = response.data.data.college_name;

    });
    $scope.$on('getCollegeRecordError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});

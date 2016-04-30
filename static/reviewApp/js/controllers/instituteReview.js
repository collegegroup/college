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

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(coachingJSONData))});

        HTTPService.POSTRequest('/review/coaching/', formData, 'coachingReview');

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
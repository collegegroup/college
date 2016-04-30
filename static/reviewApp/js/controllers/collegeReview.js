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

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(collegeJSONData))});

        HTTPService.POSTRequest('/review/college/', formData, 'collegeReview');

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

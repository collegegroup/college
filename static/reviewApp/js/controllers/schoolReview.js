/**
 * Created by bhanu on 26/4/16.
 */


var schoolReviewApp = angular.module('mainCollegeApp.schoolReview', ['starRating']);

schoolReviewApp.controller('schoolReviewCtrl', function($scope, HTTPService, utilityService, $stateParams) {

    console.log('Acadamy id: ', $stateParams.acadamyID);

    $scope.schoolID = $stateParams.acadamyID;

    $scope.schoolJSONData = {
        
        user_id: "",
        
        school_id: $scope.schoolID,
        
        school_name: "",
        
        state_name: "",
        
        class: "",
        
        stream:"",
        
        board: "",
        
        year: "",
        
        fee: "",
        
        review: "",
        
        faculties: 1,
        
        infrastructure: 1,
        
        facilities: 1,
        
        extra_curriculum: 1,
        
        social_life: 1
    };




    







    /*
    * THis is used get particluar  school record
    * */
    HTTPService.GETRequest('/school/'+$scope.schoolID+'/', '', 'getSchoolRecord');
    /*
     * THis is used get particluar  school record
     * */








    /*
    * This method is used to submit school review
    * */
    $scope.submitSchoolReview = function (schoolJSONData) {

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(schoolJSONData))});

        HTTPService.POSTRequest('/review/school/', formData, 'schoolReview');

    };
    /*
    * This method is used to submit school review
    * */









    /*
     * This is for submit review response
     * */
    $scope.$on('schoolReviewSuccess', function (event, response) {

        console.log('Response: ', response);

    });
    $scope.$on('schoolReviewError', function (event, response) {

    });
    /*
     * This is for submit review response
     * */








    /*
     * This is for get school categories response
     * */
    $scope.$on('getSchoolRecordSuccess', function (event, response) {

        console.log('Respons: ', response.data.data.school_name);

        $scope.schoolJSONData.school_name = response.data.data.school_name;

    });
    $scope.$on('getSchoolRecordError', function (event, response) {

    });
    /*
     * This is for get school categories response
     * */

});
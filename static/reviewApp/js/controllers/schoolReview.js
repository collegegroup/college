/**
 * Created by bhanu on 26/4/16.
 */


var schoolReviewApp = angular.module('mainCollegeApp.schoolReview', []);

schoolReviewApp.controller('schoolReviewCtrl', function($scope, HTTPService, utilityService, $stateParams) {

    console.log('Acadamy id: ', $stateParams.acadamyID);

    $scope.schoolID = $stateParams.acadamyID;


    $scope.schoolJSONData = {
        
        user_id: "",
        
        school_id: '',
        
        school_name: "",
        
        state_name: "",
        
        class: "",
        
        stream:"",
        
        board: "",
        
        year: "",
        
        fee: "",
        
        review: "",
        
        faculties: 0,
        
        infrastructure: 0,
        
        facilities: 0,
        
        extra_curriculum: 0,
        
        social_life: 0
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

        console.log('Respons: ', response);

    });
    $scope.$on('getSchoolRecordError', function (event, response) {

    });
    /*
     * This is for get school categories response
     * */

});
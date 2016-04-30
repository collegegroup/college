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



    $scope.schoolNameError = false;
    $scope.classNameError = false;
    $scope.streamNameError = false;
    $scope.yearError = false;
    $scope.boardError = false;
    $scope.feeError = false;

    $scope.feeFocus = false;
    $scope.boardFocus = false;
    $scope.yearFocus = false;
    $scope.streamNameFocus = false;
    $scope.classNameFocus = false;
    $scope.schoolNameFocus = false;









    /*
     * This method is used to prepare school json data
     * */
    $scope.prepareSchoolJSONData = function (jsonData) {

        $scope.schoolJSONData.faculties = jsonData.faculties.toString();
        $scope.schoolJSONData.infrastructure = jsonData.infrastructure.toString();
        $scope.schoolJSONData.facilities = jsonData.facilities.toString();
        $scope.schoolJSONData.extra_curriculum = jsonData.extra_curriculum.toString();
        $scope.schoolJSONData.social_life = jsonData.social_life.toString();

        return $scope.schoolJSONData;

    };
    /*
     * This method is used to prepare school json data
     * */
    
    
    
    
    
    
    
    
    
    
    /*
    * These are the validation methods for school JSON
    * */
    $scope.validateSchoolName = function (schoolName) {

        if(utilityService.validateText(schoolName, "SCHOOL REVIEW SCHOOL NAME VALIDATION")) {

            $scope.schoolNameError = false;
            $scope.schoolNameFocus = false;

            return true;

        }  else {

            $scope.schoolNameError = true;
            $scope.schoolNameFocus = true;

            return false;

        }

    };

    $scope.validateClass = function (className) {

        if(utilityService.validateText(className, "SCHOOL REVIEW CLASS VALIDATION")) {

            $scope.classNameError = false;
            $scope.classNameFocus = false;

            return true;

        }  else {

            $scope.classNameError = true;
            $scope.classNameFocus = true;

            return false;

        }

    };

    $scope.validateStream = function (stream) {

        if(utilityService.validateText(stream, "SCHOOL REVIEW STREAM VALIDATION")) {

            $scope.streamNameError = false;
            $scope.streamNameFocus = false;

            return true;

        }  else {

            $scope.streamNameError = true;
            $scope.streamNameFocus = true;

            return false;

        }

    };

    $scope.validateYear = function (year) {

        if(utilityService.validateText(year, "SCHOOL YEAR VALIDATION")) {

            $scope.yearError = false;
            $scope.yearFocus = false;

            return true;

        }  else {

            $scope.yearError = true;
            $scope.yearFocus = true;

            return false;

        }

    };

    $scope.validateBoard = function (board) {

        if(utilityService.validateText(board, "SCHOOL BOARD VALIDATION")) {

            $scope.boardError = false;
            $scope.boardFocus = false;

            return true;

        }  else {

            $scope.boardError = true;
            $scope.boardFocus = true;

            return false;

        }

    };

    $scope.validateFee = function (fee) {

        if(utilityService.validateText(fee, "SCHOOL FEE VALIDATION")) {

            $scope.feeError = false;
            $scope.feeFocus = false;

            return true;

        }  else {

            $scope.feeError = true;
            $scope.feeFocus = true;

            return false;

        }

    };
    /*
    * These are the validation methods for school JSON
    * */
    
    
    
    
    
    
    
    
    
    
    
    /*
    * This method is used to validate the JSON data
    * */
    $scope.validateSchoolJSONData = function (jsonData) {
      
        if($scope.validateSchoolName(jsonData.school_name) &&
            $scope.validateClass(jsonData.class) &&
            $scope.validateStream(jsonData.stream) &&
            $scope.validateYear(jsonData.year) &&
            $scope.validateBoard(jsonData.board) &&
            $scope.validateFee(jsonData.fee)) {

            jsonData = $scope.prepareSchoolJSONData(jsonData);
            
            return true;
            
        } else {
            
            return false;
            
        }
        
    };
    /*
    * This method is used to validate the JSON data
    * */




    







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
        
        if($scope.validateSchoolJSONData(schoolJSONData)) {

            var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(schoolJSONData))});

            HTTPService.POSTRequest('/review/school/', formData, 'schoolReview');
            
        }        

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
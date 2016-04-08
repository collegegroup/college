/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingRegistrationApp', []);

app.controller('coachingRegistrationCtrl', function($scope, uploadService, HTTPService, utilityService) {

    console.log('Loaded coaching registration controller.');
    
    $scope.coachingImageURL = '/media/site/logo_dummy.png';

    $scope.coachingImageUploadURL = '/upload/coaching/';
    
    $scope.hideCoachingCoureseRemoveButton = true;

    $scope.coachingRegistrationJSON =
    {
        data: {
            institute_name: "nist",
            director_name: "ramesh kumar",
            location: "vizag",
            establishment: "2001",
            description: "description",
            affiliation: "au",
            website: "nistvizag.com",
            address: "vizag",
            landline_num: "123456789",
            mobile_num: "1234567890",
            emailid: "a@a.com",
            facilities: [
                {
                    value: 1,
                    text: "Ac"
                },
                {
                    value: 0,
                    text: "Mineral Water"
                },
                {
                    value: 1,
                    text: "Bus"
                }
            ],
            profile_image: "",
            courses: [
                {
                    course: "C",
                    duration: "3 months",
                    fee: "3000"
                }
            ]
        }
    };


    /*
     * This method is used select the file
     * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.coachingImageUploadURL, fileType, 'coachingImageUpload');

    };
    /*
     * This method is used select the file
     * */








    /*
    * THis is used to handling coacing course
    * */
    $scope.addCoachingCourse = function () {console.log($scope.coachingRegistrationJSON.data.courses.length);

        $scope.coachingRegistrationJSON.data.courses.push({course: "", duration: "", fee: ""});

        if($scope.coachingRegistrationJSON.data.courses.length >= 2) {

            $scope.hideCoachingCoureseRemoveButton = false;

        }

    };
    $scope.removeCoachingCourse = function (index) {

        $scope.coachingRegistrationJSON.data.courses.splice(index, 1);
        
        if($scope.coachingRegistrationJSON.data.courses.length <= 1) {

            $scope.hideCoachingCoureseRemoveButton = true;
            
        }

    };
    /*
    * THis is used to add coacing course
    * */







    /*
    * This method is used to save coaching resistration
    * */
    $scope.saveCoachingRegistration = function(coachingObj) {

        HTTPService.POSTRequest('/register/coaching', ((JSON.stringify(coachingObj))));

    };
    /*
    * This method is used to save coaching resistration
    * */








    /*
    * This is for upload coaching image response
    * */
    $scope.$on('coachingImageUploadSuccess', function (event, response) { 

        if(response.status == "success"){

            $scope.coachingImageURL = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('coachingImageUploadError', function (event, response) {

    });
    /*
    * This is for upload coaching image response
    * */

});


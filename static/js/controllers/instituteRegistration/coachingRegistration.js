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
            institute_name: "",
            director_name: "",
            location: "",
            establishment: "",
            description: "",
            affiliation: "",
            website: "",
            address: "",
            landline_num: "",
            mobile_num: "",
            emailid: "",
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
                    course: "",
                    duration: "",
                    fee: ""
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
    * This method is used to reset the coaching registration form
    * */
    $scope.resetCoachingRegistrationForm = function() {

        $scope.coachingRegistrationJSON =
        {
            data: {
                institute_name: "",
                director_name: "",
                location: "",
                establishment: "",
                description: "",
                affiliation: "",
                website: "",
                address: "",
                landline_num: "",
                mobile_num: "",
                emailid: "",
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
                        course: "",
                        duration: "",
                        fee: ""
                    }
                ]
            }
        };

    };
    /*
    * This method is used to reset the coaching registration form
    * */









    /*
    * This method is used to save coaching resistration
    * */
    $scope.saveCoachingRegistration = function(coachingObj) {

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(coachingObj))});

        HTTPService.POSTRequest('/register/coaching/', formData, 'coachingRegistration');

    };
    /*
    * This method is used to save coaching resistration
    * */








    /*
    * This is for registration coaching response
    * */
    $scope.$on('coachingRegistrationSuccess', function (event, response) {

        $scope.resetCoachingRegistrationForm();

    });
    $scope.$on('coachingRegistrationError', function (event, response) {

    });
    /*
    * This is for registration coaching response
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


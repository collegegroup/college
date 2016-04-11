/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.schoolRegistrationApp', ['angularFileUpload']);

app.controller('schoolRegistrationCtrl', function($scope, uploadService, utilityService, HTTPService) {

    console.log('Loaded school registration controller.');

    $scope.schoolRegistrationJSON = {

        data:{
            school_name: "NIST SCHOOL",
            location: "AKP",
            establishment: "2001",
            description: "DEC",
            affiliation: "CBSE",
            website: "example.com",
            school_start_time: "10:00",
            school_end_time: "04:00",
            address: "address",
            landline_num: "landline_num",
            mobile_num: "0213125469",
            emailid: "emailid",
            facilities: [
                {
                    text: "AC",
                    value: 0
                },
                {
                    text: "BUS",
                    value: 1
                }
            ],
            profile_image: "/media/profiles/school/1.jpg",
            extra_curriculum: [
                {
                    text: "sports",
                    value: 1
                },
                {
                    text: "yoga",
                    value: 0
                }
            ]
        }
    };

    $scope.schoolImageURL = '/media/site/logo_dummy.png';

    $scope.shcoolImageUploadURL = '/upload/school/';

    /*
    * This method is used select the file
    * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.shcoolImageUploadURL, fileType, 'schoolImageUpload');

    };
    /*
    * This method is used select the file
    * */








    /*
     * This method is used to reset the school registration form
     * */
    $scope.resetSchoolRegistrationForm = function() {

        $scope.schoolRegistrationJSON = {

            data:{
                school_name: "NIST SCHOOL",
                location: "AKP",
                establishment: "2001",
                description: "DEC",
                affiliation: "CBSE",
                website: "example.com",
                school_start_time: "10:00",
                school_end_time: "04:00",
                address: "address",
                landline_num: "landline_num",
                mobile_num: "0213125469",
                emailid: "emailid",
                facilities: [
                    {
                        text: "AC",
                        value: 0
                    },
                    {
                        text: "BUS",
                        value: 1
                    }
                ],
                profile_image: "/media/profiles/school/1.jpg",
                extra_curriculum: [
                    {
                        text: "sports",
                        value: 1
                    },
                    {
                        text: "yoga",
                        value: 0
                    }
                ]
            }
        };

    };
    /*
     * This method is used to reset the school registration form
     * */









    /*
     * This method is used to save coaching resistration
     * */
    $scope.saveSchoolRegistration = function(schoolObj) {

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(schoolObj))});

        HTTPService.POSTRequest('/register/school/', formData, 'schoolRegistration');

    };
    /*
     * This method is used to save coaching resistration
     * */








    /*
     * This is for registration coaching response
     * */
    $scope.$on('schoolRegistrationSuccess', function (event, response) {

        $scope.resetSchoolRegistrationForm();

    });
    $scope.$on('schoolRegistrationError', function (event, response) {

    });
    /*
     * This is for registration coaching response
     * */







    /*
     * This is for upload college image response
     * */
    $scope.$on('schoolImageUploadSuccess', function (event, response) {

        if(response.status == "success"){

            $scope.schoolImageURL = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('schoolImageUploadError', function (event, response) {

    });
    /*
     * This is for upload college image response
     * */

});


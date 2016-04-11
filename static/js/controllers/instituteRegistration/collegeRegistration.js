/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.collegeRegistrationApp', []);

app.controller('collegeRegistrationCtrl', function($scope, uploadService, utilityService, HTTPService) {

    $scope.collegeRegistrationJSON ={
        data: {
            college_name:"nist",
            location:"vizag",
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
            highest_package: "320000",
            average_package:"150000",
            courses:[
                {
                    course:"MBA",
                    duration:"2 yr",
                    fee:"100000",
                    entrance:"ICET"
                }
            ]
        }
    };

    $scope.collegeImageURL = '/media/site/logo_dummy.png';

    $scope.collegeImageUploadURL = '/upload/college/';

    $scope.hideCollegeCoureseRemoveButton = true;

    /*
     * This method is used select the file
     * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.collegeImageUploadURL, fileType, 'collegeImageUpload');

    };
    /*
     * This method is used select the file
     * */







    /*
     * THis is used to handling college course
     * */
    $scope.addCollegeCourse = function () {

        $scope.collegeRegistrationJSON.data.courses.push({course: "", duration: "", fee: ""});

        if($scope.collegeRegistrationJSON.data.courses.length >= 2) {

            $scope.hideCollegeCoureseRemoveButton = false;

        }

    };
    $scope.removeCollegeCourse = function (index) {

        $scope.collegeRegistrationJSON.data.courses.splice(index, 1);

        if($scope.collegeRegistrationJSON.data.courses.length <= 1) {

            $scope.hideCollegeCoureseRemoveButton = true;

        }

    };
    /*
     * THis is used to add coacing course
     * */







    /*
     * This method is used to reset the college registration form
     * */
    $scope.resetCollegeRegistrationForm = function() {

        $scope.collegeRegistrationJSON = {
            data: {
                college_name:"nist",
                location:"vizag",
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
                highest_package: "320000",
                average_package:"150000",
                courses:[
                    {
                        course:"MBA",
                        duration:"2 yr",
                        fee:"100000",
                        entrance:"ICET"
                    }
                ]
            }
        };

    };
    /*
     * This method is used to reset the college registration form
     * */









    /*
     * This method is used to save college resistration
     * */
    $scope.saveCollegeRegistration = function(collegeObj) {

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(collegeObj))});

        HTTPService.POSTRequest('/register/college/', formData, 'collegeRegistration');

    };
    /*
     * This method is used to save college resistration
     * */








    /*
     * This is for registration college response
     * */
    $scope.$on('collegeRegistrationSuccess', function (event, response) {

        $scope.resetCollegeRegistrationForm();

    });
    $scope.$on('collegeRegistrationError', function (event, response) {

    });
    /*
     * This is for registration college response
     * */








    /*
     * This is for upload college image response
     * */
    $scope.$on('collegeImageUploadSuccess', function (event, response) {

        if(response.status == "success"){

            $scope.collegeImageURL = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('collegeImageUploadError', function (event, response) {

    });
    /*
     * This is for upload college image response
     * */

});


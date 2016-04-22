/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.collegeRegistrationApp', []);

app.controller('collegeRegistrationCtrl', function($scope, uploadService, utilityService, HTTPService) {

    /* Form validation variables */
    $scope.collegeNameError = false;

    $scope.collegeLocationError = false;

    $scope.collegeEstablishmentError = false;

    $scope.collegeDescriptionError = false;

    $scope.collegeAddressError = false;

    $scope.collegeAffiliationError = false;

    $scope.collegeMobileNoError = false;

    $scope.collegeWebsiteError = false;

    $scope.collegeEmailError = false;

    $scope.collegeCoursesError = false;
    /* Form validation variables */

    /* Form validation variables */
    $scope.collegeNameFocus = false;

    $scope.collegeDirectorNameFocus = false;

    $scope.collegeLocationFocus = false;

    $scope.collegeEstablishmentFocus = false;

    $scope.collegeDescriptionFocus = false;

    $scope.collegeAddressFocus = false;

    $scope.collegeAffiliationFocus = false;

    $scope.collegeMobileNoFocus = false;

    $scope.collegeWebsiteFocus = false;

    $scope.collegeEmailFocus = false;

    $scope.collegeCoursesFocus = false;
    /* Form validation variables */

    $scope.collegeRegistrationJSON ={
        data: {
            college_name:"",
            location:"",
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
            highest_package: "",
            average_package:"",
            courses:[
                {
                    course:"",
                    duration:"",
                    fee:"",
                    entrance:""
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
                college_name:"",
                location:"",
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
                highest_package: "",
                average_package:"",
                courses:[
                    {
                        course:"",
                        duration:"",
                        fee:"",
                        entrance:""
                    }
                ]
            }
        };

    };
    /*
     * This method is used to reset the college registration form
     * */








    /*
     * Validation methods
     * */
    $scope.validateCollegeName = function(collegeeName) {

        if(utilityService.validateText(collegeeName, "COLLEGE NAME VALIDATION")) {

            $scope.collegeNameError = false;
            $scope.collegeNameFocus = false;

            return true;

        }  else {

            $scope.collegeNameError = true;
            $scope.collegeNameFocus = true;

            return false;

        }

    };
    $scope.validateCollegeLocation = function(locationName) {

        if(utilityService.validateText(locationName, "COLLEGE LOCATION NAME VALIDATION")) {

            $scope.collegeLocationError = false;
            $scope.collegeLocationFocus = false;

            return true;

        }  else {

            $scope.collegeLocationError = true;
            $scope.collegeLocationFocus = true;

            return false;

        }

    };
    $scope.validateCollegeEstablishment = function(establishment) {

        if(utilityService.validateNumber(establishment, "COLLEGE ESTABLISHMENT VALIDATION")) {

            $scope.collegeEstablishmentError = false;
            $scope.collegeEstablishmentFocus = false;

            return true;

        }  else {

            $scope.collegeEstablishmentError = true;
            $scope.collegeEstablishmentFocus = true;

            return false;

        }

    };
    $scope.validateCollegeDescription = function(description) {

        if(utilityService.validateText(description, "COLLEGE DESCRIPTION VALIDATION")) {

            $scope.collegeDescriptionError = false;
            $scope.collegeDescriptionFocus = false;

            return true;

        }  else {

            $scope.collegeDescriptionError = true;
            $scope.collegeDescriptionFocus = true;

            return false;

        }

    };
    $scope.validateCollegeAddress = function(address) {

        if(utilityService.validateText(address, "COLLEGE ADDRESS VALIDATION")) {

            $scope.collegeAddressError = false;
            $scope.collegeAddressFocus = false;

            return true;

        }  else {

            $scope.collegeAddressError = true;
            $scope.collegeAddressFocus = true;

            return false;

        }

    };
    $scope.validateCollegeAffiliation = function(affiliation) {

        if(utilityService.validateText(affiliation, "COLLEGE ADDRESS VALIDATION")) {

            $scope.collegeAffiliationError = false;
            $scope.collegeAffiliationFocus = false;

            return true;

        }  else {

            $scope.collegeAffiliationError = true;
            $scope.collegeAffiliationFocus = true;

            return false;

        }

    };
    $scope.validateCollegeMobileNo = function(mobileNo) {

        if(utilityService.validateText(mobileNo, "COLLEGE MOBILE NO VALIDATION")) {

            $scope.collegeMobileNoError = false;
            $scope.collegeMobileNoFocus = false;

            return true;

        }  else {

            $scope.collegeMobileNoError = true;
            $scope.collegeMobileNoFocus = true;

            return false;

        }

    };
    $scope.validateCollegeWebsite = function(website) {

        if(utilityService.validateText(website, "COLLEGE WEBSITE VALIDATION")) {

            $scope.collegeWebsiteError = false;
            $scope.collegeWebsiteFocus = false;

            return true;

        }  else {

            $scope.collegeWebsiteError = true;
            $scope.collegeWebsiteFocus = true;

            return false;

        }

    };
    $scope.validateCollegeEmail = function(emailID) {

        if(utilityService.validateEmail(emailID, "COLLEGE EMAIL ID VALIDATION")) {

            $scope.collegeEmailError = false;
            $scope.collegeEmailFocus = false;

            return true;

        }  else {

            $scope.collegeEmailError = true;
            $scope.collegeEmailFocus = true;

            return false;

        }

    };
    /*
     * Validation methods
     * */








    /*
     * This method is used to validate college registration form
     * */
    $scope.validateCollegeRegistrationForm = function(collegeObj) {

        if( $scope.validateCollegeName(collegeObj.data.college_name) &&
            $scope.validateCollegeLocation(collegeObj.data.location) &&
            $scope.validateCollegeEstablishment(collegeObj.data.establishment) &&
            $scope.validateCollegeDescription(collegeObj.data.description) &&
            $scope.validateCollegeAddress(collegeObj.data.address) &&
            $scope.validateCollegeAffiliation(collegeObj.data.affiliation) &&
            $scope.validateCollegeMobileNo(collegeObj.data.mobile_num) &&
            $scope.validateCollegeWebsite(collegeObj.data.website) &&
            $scope.validateCollegeEmail(collegeObj.data.emailid)) {

            $scope.saveCollegeRegistration(collegeObj);

        }

    };
    /*
     * This method is used to validate college registration form
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


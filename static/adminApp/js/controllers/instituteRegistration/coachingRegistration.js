/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingRegistrationApp', []);

app.controller('coachingRegistrationCtrl', function($scope, uploadService, HTTPService, utilityService) {

    console.log('Loaded coaching registration controller.');
    
    $scope.coachingImageURL = '/media/site/logo_dummy.png';

    $scope.coachingImageUploadURL = '/upload/coaching/';
    
    $scope.hideCoachingCoureseRemoveButton = true;

    /* Form validation variables */
    $scope.coachingInstituteNameError = false;

    $scope.coachingDirectorNameError = false;

    $scope.coachingLocationError = false;

    $scope.coachingEstablishmentError = false;

    $scope.coachingDescriptionError = false;

    $scope.coachingAddressError = false;

    $scope.coachingAffiliationError = false;

    $scope.coachingMobileNoError = false;

    $scope.coachingWebsiteError = false;

    $scope.coachingEmailError = false;

    $scope.coachingCoursesError = false;
    /* Form validation variables */

    /* Form validation variables */
    $scope.coachingInstituteNameFocus = false;

    $scope.coachingDirectorNameFocus = false;

    $scope.coachingLocationFocus = false;

    $scope.coachingEstablishmentFocus = false;

    $scope.coachingDescriptionFocus = false;

    $scope.coachingAddressFocus = false;

    $scope.coachingAffiliationFocus = false;

    $scope.coachingMobileNoFocus = false;

    $scope.coachingWebsiteFocus = false;

    $scope.coachingEmailFocus = false;

    $scope.coachingCoursesFocus = false;
    /* Form validation variables */

    $scope.coachingRegistrationJSON = {
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
    * Validation methods
    * */
    $scope.validateCoachingInstituteName = function(instituteName) {

        if(utilityService.validateText(instituteName, "COACHING INSTITUTE NAME VALIDATION")) {

            $scope.coachingInstituteNameError = false;
            $scope.coachingInstituteNameFocus = false;

            return true;

        }  else {

            $scope.coachingInstituteNameError = true;
            $scope.coachingInstituteNameFocus = true;

            return false;

        }

    };
    $scope.validateCoachingDirectorName = function(directorName) {

        if(utilityService.validateText(directorName, "COACHING DIRECTOR NAME VALIDATION")) {

            $scope.coachingDirectorNameError = false;
            $scope.coachingDirectorNameFocus = false;

            return true;

        }  else {

            $scope.coachingDirectorNameError = true;
            $scope.coachingDirectorNameFocus = true;

            return false;

        }

    };
    $scope.validateCoachingLocation = function(locationName) {

        if(utilityService.validateText(locationName, "COACHING LOCATION NAME VALIDATION")) {

            $scope.coachingLocationError = false;
            $scope.coachingLocationFocus = false;

            return true;

        }  else {

            $scope.coachingLocationError = true;
            $scope.coachingLocationFocus = true;

            return false;

        }

    };
    $scope.validateCoachingEstablishment = function(establishment) {

        if(utilityService.validateNumber(establishment, "COACHING ESTABLISHMENT VALIDATION")) {

            $scope.coachingEstablishmentError = false;
            $scope.coachingEstablishmentFocus = false;

            return true;

        }  else {

            $scope.coachingEstablishmentError = true;
            $scope.coachingEstablishmentFocus = true;

            return false;

        }

    };
    $scope.validateCoachingDescription = function(description) {

        if(utilityService.validateText(description, "COACHING DESCRIPTION VALIDATION")) {

            $scope.coachingDescriptionError = false;
            $scope.coachingDescriptionFocus = false;

            return true;

        }  else {

            $scope.coachingDescriptionError = true;
            $scope.coachingDescriptionFocus = true;

            return false;

        }

    };
    $scope.validateCoachingAddress = function(address) {

        if(utilityService.validateText(address, "COACHING ADDRESS VALIDATION")) {

            $scope.coachingAddressError = false;
            $scope.coachingAddressFocus = false;

            return true;

        }  else {

            $scope.coachingAddressError = true;
            $scope.coachingAddressFocus = true;

            return false;

        }

    };
    $scope.validateCoachingAffiliation = function(affiliation) {

        if(utilityService.validateText(affiliation, "COACHING ADDRESS VALIDATION")) {

            $scope.coachingAffiliationError = false;
            $scope.coachingAffiliationFocus = false;

            return true;

        }  else {

            $scope.coachingAffiliationError = true;
            $scope.coachingAffiliationFocus = true;

            return false;

        }

    };
    $scope.validateCoachingMobileNo = function(mobileNo) {

        if(utilityService.validateText(mobileNo, "COACHING MOBILE NO VALIDATION")) {

            $scope.coachingMobileNoError = false;
            $scope.coachingMobileNoFocus = false;

            return true;

        }  else {

            $scope.coachingMobileNoError = true;
            $scope.coachingMobileNoFocus = true;

            return false;

        }

    };
    $scope.validateCoachingWebsite = function(website) {

        if(utilityService.validateText(website, "COACHING WEBSITE VALIDATION")) {

            $scope.coachingWebsiteError = false;
            $scope.coachingWebsiteFocus = false;

            return true;

        }  else {

            $scope.coachingWebsiteError = true;
            $scope.coachingWebsiteFocus = true;

            return false;

        }

    };
    $scope.validateCoachingEmail = function(emailID) {

        if(utilityService.validateEmail(emailID, "COACHING EMAIL ID VALIDATION")) {

            $scope.coachingEmailError = false;
            $scope.coachingEmailFocus = false;

            return true;

        }  else {

            $scope.coachingEmailError = true;
            $scope.coachingEmailFocus = true;

            return false;

        }

    };
    /*
    * Validation methods
    * */








    /*
    * This method is used to validate coaching registration form
    * */
    $scope.validateCoachingRegistrationForm = function(coachingObj) {

        if( $scope.validateCoachingInstituteName(coachingObj.data.institute_name) &&
            $scope.validateCoachingDirectorName(coachingObj.data.director_name) &&
            $scope.validateCoachingLocation(coachingObj.data.location) &&
            $scope.validateCoachingEstablishment(coachingObj.data.establishment) &&
            $scope.validateCoachingDescription(coachingObj.data.description) &&
            $scope.validateCoachingAddress(coachingObj.data.address) &&
            $scope.validateCoachingAffiliation(coachingObj.data.affiliation) &&
            $scope.validateCoachingMobileNo(coachingObj.data.mobile_num) &&
            $scope.validateCoachingWebsite(coachingObj.data.website) &&
            $scope.validateCoachingEmail(coachingObj.data.emailid)) {

            $scope.saveCoachingRegistration(coachingObj);

        }

    };
    /*
    * This method is used to validate coaching registration form
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

            $scope.coachingRegistrationJSON.data.profile_image = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('coachingImageUploadError', function (event, response) {

    });
    /*
     * This is for upload coaching image response
     * */

});


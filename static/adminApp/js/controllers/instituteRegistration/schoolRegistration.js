/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.schoolRegistrationApp', ['angularFileUpload', 'dnTimepicker']);

app.controller('schoolRegistrationCtrl', function($scope, uploadService, utilityService, HTTPService) {


    /* Form validation variables */
    $scope.schoolNameError = false;

    $scope.schoolLocationError = false;

    $scope.schoolEstablishmentError = false;

    $scope.schoolDescriptionError = false;

    $scope.schoolAddressError = false;

    $scope.schoolAffiliationError = false;

    $scope.schoolMobileNoError = false;

    $scope.schoolWebsiteError = false;

    $scope.schoolEmailError = false;
    /* Form validation variables */

    /* Form validation variables */
    $scope.schoolNameError = false;

    $scope.schoolLocationFocus = false;

    $scope.schoolEstablishmentFocus = false;

    $scope.schoolDescriptionFocus = false;

    $scope.schoolAddressFocus = false;

    $scope.schoolAffiliationFocus = false;

    $scope.schoolMobileNoFocus = false;

    $scope.schoolWebsiteFocus = false;

    $scope.schoolEmailFocus = false;
    /* Form validation variables */

    $scope.today = new Date();

    $scope.schoolRegistrationJSON = {

        data:{
            school_name: "",
            location: "",
            establishment: "",
            description: "",
            affiliation: "",
            website: "",
            school_start_time: $scope.today,
            school_end_time: $scope.today,
            address: "",
            landline_num: "",
            mobile_num: "",
            emailid: "",
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
                    text: "Yoga",
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
                school_name: "",
                location: "",
                establishment: "",
                description: "",
                affiliation: "",
                website: "",
                school_start_time: $scope.today,
                school_end_time: $scope.today,
                address: "address",
                landline_num: "",
                mobile_num: "",
                emailid: "",
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
     * Validation methods
     * */
    $scope.validateSchoolName = function(schoolName) {

        if(utilityService.validateText(schoolName, "SCHOOL NAME VALIDATION")) {

            $scope.schoolNameError = false;
            $scope.schoolNameFocus = false;

            return true;

        }  else {

            $scope.schoolNameError = true;
            $scope.schoolNameFocus = true;

            return false;

        }

    };
    $scope.validateSchoolLocation = function(locationName) {

        if(utilityService.validateText(locationName, "SCHOOL LOCATION NAME VALIDATION")) {

            $scope.schoolLocationError = false;
            $scope.schoolLocationFocus = false;

            return true;

        }  else {

            $scope.schoolLocationError = true;
            $scope.schoolLocationFocus = true;

            return false;

        }

    };
    $scope.validateSchoolEstablishment = function(establishment) {

        if(utilityService.validateNumber(establishment, "SCHOOL ESTABLISHMENT VALIDATION")) {

            $scope.schoolEstablishmentError = false;
            $scope.schoolEstablishmentFocus = false;

            return true;

        }  else {

            $scope.schoolEstablishmentError = true;
            $scope.schoolEstablishmentFocus = true;

            return false;

        }

    };
    $scope.validateSchoolDescription = function(description) {

        if(utilityService.validateText(description, "SCHOOL DESCRIPTION VALIDATION")) {

            $scope.schoolDescriptionError = false;
            $scope.schoolDescriptionFocus = false;

            return true;

        }  else {

            $scope.schoolDescriptionError = true;
            $scope.schoolDescriptionFocus = true;

            return false;

        }

    };
    $scope.validateSchoolAddress = function(address) {

        if(utilityService.validateText(address, "SCHOOL ADDRESS VALIDATION")) {

            $scope.schoolAddressError = false;
            $scope.schoolAddressFocus = false;

            return true;

        }  else {

            $scope.schoolAddressError = true;
            $scope.schoolAddressFocus = true;

            return false;

        }

    };
    $scope.validateSchoolAffiliation = function(affiliation) {

        if(utilityService.validateText(affiliation, "SCHOOL ADDRESS VALIDATION")) {

            $scope.schoolAffiliationError = false;
            $scope.schoolAffiliationFocus = false;

            return true;

        }  else {

            $scope.schoolAffiliationError = true;
            $scope.schoolAffiliationFocus = true;

            return false;

        }

    };
    $scope.validateSchoolMobileNo = function(mobileNo) {

        if(utilityService.validateText(mobileNo, "SCHOOL MOBILE NO VALIDATION")) {

            $scope.schoolMobileNoError = false;
            $scope.schoolMobileNoFocus = false;

            return true;

        }  else {

            $scope.schoolMobileNoError = true;
            $scope.schoolMobileNoFocus = true;

            return false;

        }

    };
    $scope.validateSchoolWebsite = function(website) {

        if(utilityService.validateText(website, "SCHOOL WEBSITE VALIDATION")) {

            $scope.schoolWebsiteError = false;
            $scope.schoolWebsiteFocus = false;

            return true;

        }  else {

            $scope.schoolWebsiteError = true;
            $scope.schoolWebsiteFocus = true;

            return false;

        }

    };
    $scope.validateSchoolEmail = function(emailID) {

        if(utilityService.validateEmail(emailID, "SCHOOL EMAIL ID VALIDATION")) {

            $scope.schoolEmailError = false;
            $scope.schoolEmailFocus = false;

            return true;

        }  else {

            $scope.schoolEmailError = true;
            $scope.schoolEmailFocus = true;

            return false;

        }

    };
    /*
     * Validation methods
     * */









    /*
     * This method is used to validate school registration form
     * */
    $scope.validateSchoolRegistrationForm = function(schoolObj) {

        if( $scope.validateSchoolName(schoolObj.data.school_name) &&
            $scope.validateSchoolLocation(schoolObj.data.location) &&
            $scope.validateSchoolEstablishment(schoolObj.data.establishment) &&
            $scope.validateSchoolDescription(schoolObj.data.description) &&
            $scope.validateSchoolAddress(schoolObj.data.address) &&
            $scope.validateSchoolAffiliation(schoolObj.data.affiliation) &&
            $scope.validateSchoolMobileNo(schoolObj.data.mobile_num) &&
            $scope.validateSchoolWebsite(schoolObj.data.website) &&
            $scope.validateSchoolEmail(schoolObj.data.emailid)) {

            $scope.schoolRegistrationJSON = $scope.prepareSchoolRegistrationJSON(schoolObj);

            $scope.saveSchoolRegistration($scope.schoolRegistrationJSON);

        }

    };
    /*
     * This method is used to validate school registration form
     * */

    
    
    
    
    
    
    
    
    /*
    * This method is used to prepare school registration JSON
    * */
    $scope.prepareSchoolRegistrationJSON = function (schoolJSON) {
      
        console.log(utilityService.convertTimeStringTo24HoursFormat(schoolJSON.data.school_start_time));

        $scope.schoolRegistrationJSON.data.school_start_time = utilityService.convertTimeStringTo24HoursFormat(schoolJSON.data.school_start_time);

        $scope.schoolRegistrationJSON.data.school_end_time = utilityService.convertTimeStringTo24HoursFormat(schoolJSON.data.school_end_time);

        return $scope.schoolRegistrationJSON;

    };
    /*
    * This method is used to prepare school registration JSON
    * */











    /*
     * This method is used to save school resistration
     * */
    $scope.saveSchoolRegistration = function(schoolObj) {

        var formData = utilityService.objectToRequestData({jsonData: encodeURIComponent(JSON.stringify(schoolObj))});

        HTTPService.POSTRequest('/register/school/', formData, 'schoolRegistration');

    };
    /*
     * This method is used to save school resistration
     * */








    /*
     * This is for registration school response
     * */
    $scope.$on('schoolRegistrationSuccess', function (event, response) {

        $scope.resetSchoolRegistrationForm();

    });
    $scope.$on('schoolRegistrationError', function (event, response) {

    });
    /*
     * This is for registration school response
     * */







    /*
     * This is for upload school image response
     * */
    $scope.$on('schoolImageUploadSuccess', function (event, response) {

        if(response.status == "success"){

            $scope.schoolImageURL = response.profile_image_path;

            $scope.schoolRegistrationJSON.data.profile_image = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('schoolImageUploadError', function (event, response) {

    });
    /*
     * This is for upload school image response
     * */

});


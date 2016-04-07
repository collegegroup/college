/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.schoolRegistrationApp', ['angularFileUpload']);

app.controller('schoolRegistrationCtrl', function($scope, uploadService) {

    console.log('Loaded school registration controller.');

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


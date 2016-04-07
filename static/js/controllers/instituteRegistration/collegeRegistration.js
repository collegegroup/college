/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.collegeRegistrationApp', []);

app.controller('collegeRegistrationCtrl', function($scope, uploadService) {

    console.log('Loaded school registration controller.');

    $scope.collegeImageURL = '/media/site/logo_dummy.png';

    $scope.collegeImageUploadURL = '/upload/college/';

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


/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.collegeRegistrationApp', []);

app.controller('collegeRegistrationCtrl', function($scope) {

    console.log('Loaded school registration controller.');

    $scope.collegeImageUploadURL = '/upload/college';

    /*
     * This method is used select the file
     * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.collegeImageUploadURL, fileType);

    };
    /*
     * This method is used select the file
     * */

});


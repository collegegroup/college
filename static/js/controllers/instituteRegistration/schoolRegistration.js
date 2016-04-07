/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.schoolRegistrationApp', ['angularFileUpload']);

app.controller('schoolRegistrationCtrl', function($scope, uploadService) {

    console.log('Loaded school registration controller.');

    $scope.shcoolImageUploadURL = '/upload/school';

    /*
    * This method is used select the file
    * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.shcoolImageUploadURL, fileType);

    };
    /*
    * This method is used select the file
    * */

});


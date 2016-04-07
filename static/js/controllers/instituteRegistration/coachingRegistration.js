/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingRegistrationApp', []);

app.controller('coachingRegistrationCtrl', function($scope, uploadService) {

    console.log('Loaded coaching registration controller.');

    $scope.coachingImageUploadURL = '/upload/coaching/';

    /*
     * This method is used select the file
     * */
    $scope.onFileSelect = function (fileObj, fileType) {

        console.log(fileObj, fileType);

        uploadService.uploadFile(fileObj, $scope.coachingImageUploadURL, fileType);

    };
    /*
     * This method is used select the file
     * */

});


/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingRegistrationApp', []);

app.controller('coachingRegistrationCtrl', function($scope, uploadService) {

    console.log('Loaded coaching registration controller.');
    
    $scope.coachingImageURL = '/media/site/logo_dummy.png';

    $scope.coachingImageUploadURL = '/upload/coaching/';

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
    * This is for upload coaching image response
    * */
    $scope.$on('coachingImageUpload success', function (event, response) {

        if(response.status == "success"){

            $scope.coachingImageURL = response.profile_image_path;

        } else {

        }

    });
    $scope.$on('coachingImageUpload error', function (event, response) {

    });
    /*
    * This is for upload coaching image response
    * */

});


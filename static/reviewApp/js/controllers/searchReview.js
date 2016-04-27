/**
 * Created by bhanu on 26/4/16.
 */

var searchReviewApp = angular.module('mainCollegeApp.searchReview', []);

searchReviewApp.controller('searchReviewCtrl', function($scope, HTTPService, utilityService) {

    $scope.searchQuery = '';



    /*
     * This for get all academy details
     * */
    $scope.getRecords = function (searchQuery) {

        var formData = utilityService.objectToRequestData({name_prefix: searchQuery});

        HTTPService.POSTRequest('/review/search/', formData, 'getAllAcademyDetails');

    };
    /*
     * This for get call all academy details
     * */







    /*
     * This is for get all academy details success response
     * */
    $scope.$on('getAllAcademyDetailsSuccess', function (event, response) {

        console.log('REsp: ', response);

    });
    $scope.$on('getAllAcademyDetailsError', function (event, response) {

    });
    /*
     * This is for get all academy details success response
     * */

});

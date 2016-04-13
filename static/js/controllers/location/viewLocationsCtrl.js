
var app = angular.module('mainCollegeApp.viewLocationsApp', []);

app.controller('viewLocationsCtrl', function($scope, HTTPService, utilityService) {

    $scope.allLocations = [];

    $scope.searchLocations = '';

    /*
     * This for get locations
     * */
    HTTPService.GETRequest('/alllocation/', '', 'getAllLocations');
    /*
     * This for get locations
     * */








    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getAllLocationsSuccess', function (event, response) {

        console.log('coachingCategoriesCourses: ', response);

        $scope.allLocations = response.data.data.locations;

    });
    $scope.$on('getAllLocationsError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});
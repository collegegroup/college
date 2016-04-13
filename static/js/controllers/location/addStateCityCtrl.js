
var app = angular.module('mainCollegeApp.addStateCityApp', []);

app.controller('addStateCityCtrl', function($scope, HTTPService, utilityService) {

    $scope.allStates = [];

    $scope.state = '';

    $scope.city = '';

    /*
     * This for get states categories
     * */
    HTTPService.GETRequest('/allstate/', '', 'getStatesFromAddStateCity');
    /*
     * This for get states categories
     * */








    /*
     * This method is used to add city category
     * */
    $scope.addCity = function(city, state) {

        var formData = utilityService.objectToRequestData({state_name: state, city_name: city});

        HTTPService.POSTRequest('/addcity/', formData, 'addCity');

    };
    /*
     * This method is used to add city category
     * */








    /*
     * This is for add city response
     * */
    $scope.$on('addCitySuccess', function (event, response) {

        $scope.state = '';

        $scope.city = '';

    });
    $scope.$on('addCityError', function (event, response) {

    });
    /*
     * This is for add city response
     * */







    /*
     * This is for get states categories response
     * */
    $scope.$on('getStatesFromAddStateCitySuccess', function (event, response) {

        $scope.allStates = response.data.data.states;

    });
    $scope.$on('getStatesFromAddStateCityError', function (event, response) {

    });
    /*
     * This is for get states categories response
     * */

});
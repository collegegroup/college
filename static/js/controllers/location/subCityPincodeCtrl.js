/**
 * Created by bhanu on 5/4/16.
 */

var app = angular.module('mainCollegeApp.subCityPincodeApp', []);

app.controller('subCityPincodeCtrl', function($scope, HTTPService, utilityService) {

    $scope.cities = [];

    $scope.states = [];

    $scope.location = '';

    $scope.city = '';

    $scope.state = '';

    $scope.pincode = '';

    /*
     * This for get states and cities
     * */
    HTTPService.GETRequest('/allcity/', '', 'getCities');

    HTTPService.GETRequest('/allstate/', '', 'getStatesFromSubCityPincode');
    /*
     * This for get states and cities
     * */






    /*
     * This method is used to add location
     * */
    $scope.addLocation = function(city, state, location, pincode) {

        var formData = utilityService.objectToRequestData(
            {
                state_name: state,
                city_name: city,
                location_name: location,
                pin_code: pincode
            });

        HTTPService.POSTRequest('/addlocation/', formData, 'addLocation');

    };
    /*
     * This method is used to add location
     * */








    /*
     * This is for add location response
     * */
    $scope.$on('addLocationSuccess', function (event, response) {

        $scope.location = '';

        $scope.city = '';

        $scope.state = '';

        $scope.pincode = '';

    });
    $scope.$on('addLocationError', function (event, response) {

    });
    /*
     * This is for add location response
     * */








    /*
     * This is for get cities categories response
     * */
    $scope.$on('getCitiesSuccess', function (event, response) {

        console.log(response);

        $scope.cities = response.data.data.cities;

    });
    $scope.$on('getCitiesError', function (event, response) {

    });
    /*
     * This is for get cities categories response
     * */
    /*
     * This is for get cities categories response
     * */
    $scope.$on('getStatesFromSubCityPincodeSuccess', function (event, response) {

        console.log(response);

        $scope.states = response.data.data.states;

    });
    $scope.$on('getStatesFromSubCityPincodeError', function (event, response) {

    });
    /*
     * This is for get cities categories response
     * */

});
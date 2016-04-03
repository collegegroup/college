
var app = angular.module('collegeMainApp', ['ngRoute']);

app.controller('collegeMainCtrl', function($scope) {

    console.log('Its working perfect');

});

app.config(['$routeProvider',function($routeProvider) {

    $routeProvider.

        when('/dashboard', {

            templateUrl: 'static/templates/dashboard.html'

        }).

        when('/', {

            templateUrl: 'static/templates/dashboard.html'

        }).

        when('/location/statecity', {

            templateUrl: 'static/templates/AddStateCity.html'/*,
            controller: 'RouteController'*/

        }).
        when('/location/statepin', {

            templateUrl: 'static/templates/AddSubCityPin.html'/*,
            controller: 'RouteController'*/

        }).
         when('/location/view', {

            templateUrl: 'static/templates/ViewLocations.html'/*,
            controller: 'RouteController'*/

        }).
        otherwise({

            redirectTo: '/'

        });
}]);
/**
 * Created by bhanu on 5/4/16.
 */

var collegeApp = angular.module('mainCollegeApp');

collegeApp.config([ "$stateProvider", "$urlRouterProvider",

    function($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/home');

        $stateProvider

            .state('location statecity', {

                url: '/location/statecity',

                templateUrl: 'static/templates/locationManagement/AddStateCity.html'

            })

            .state('location subcity pincode', {

                url: '/location/statepin',

                templateUrl: 'static/templates/locationManagement/AddSubCityPin.html'

            })

            .state('location view', {

                url: '/location/view',

                templateUrl: 'static/templates/locationManagement/ViewLocations.html'

            })






            /*From here course management routes*/
            .state('course management college', {

                url: '/coursemanagement/college',

                templateUrl: 'static/templates/courseManagement/CollegeMaster.html'

            })

            .state('course management coaching', {

            url: '/coursemanagement/coaching',

            templateUrl: 'static/templates/courseManagement/CoachingMaster.html'

        });

    }]);

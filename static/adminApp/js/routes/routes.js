/**
 * Created by bhanu on 5/4/16.
 */

var collegeApp = angular.module('mainCollegeApp');

collegeApp.config([ "$stateProvider", "$urlRouterProvider",

    function($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/dashboard');

        $stateProvider
            
            .state('Dashboard', {

                url: '/dashboard',

                templateUrl: 'static/adminApp/templates/dashboard/dashboard.html',

                controller: 'dashboardCtrl'

            })
            
            
            
            
            /*From here location management routes*/
            .state('location statecity', {

                url: '/location/statecity',

                templateUrl: 'static/adminApp/templates/locationManagement/AddStateCity.html',

                controller: 'addStateCityCtrl'

            })

            .state('location subcity pincode', {

                url: '/location/statepin',

                templateUrl: 'static/adminApp/templates/locationManagement/AddSubCityPin.html',

                controller: 'subCityPincodeCtrl'

            })

            .state('location view', {

                url: '/location/view',

                templateUrl: 'static/adminApp/templates/locationManagement/ViewLocations.html',

                controller: 'viewLocationsCtrl'

            })






            /*From here course management routes*/
            .state('course management college', {

                url: '/coursemanagement/college',

                templateUrl: 'static/adminApp/templates/courseManagement/CollegeMaster.html',

                controller: 'collegeManagementCtrl'

            })

            .state('course management coaching', {

                url: '/coursemanagement/coaching',

                templateUrl: 'static/adminApp/templates/courseManagement/CoachingMaster.html',

                controller: 'coachingManagementCtrl'

            })




            /*From here institute registration routes*/
            .state('Institute registration school', {

                url: '/instituteregistration/school',

                templateUrl: 'static/adminApp/templates/instituteRegistration/SchoolRegistration.html',

                controller: 'schoolRegistrationCtrl'

            })

            .state('Institute registration college', {

                url: '/instituteregistration/college',

                templateUrl: 'static/adminApp/templates/instituteRegistration/CollegeRegistration.html',

                controller: 'collegeRegistrationCtrl'

            })

            .state('Institute registration coaching', {

                url: '/instituteregistration/coaching',

                templateUrl: 'static/adminApp/templates/instituteRegistration/CoachingRegistration.html',

                controller: 'coachingRegistrationCtrl'

            });

    }]);

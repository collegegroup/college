(function(angular){
    'use strict';

    var collgeApp = angular.module('mainCollegeApp', ['ui.router',
                                                'mainCollegeApp.dashboard',

                                                'mainCollegeApp.addStateCityApp',
                                                'mainCollegeApp.subCityPincodeApp',
                                                'mainCollegeApp.viewLocationsApp',

                                                'mainCollegeApp.collegeManagementApp',
                                                'mainCollegeApp.coachingManagementApp',

                                                'mainCollegeApp.schoolRegistrationApp',
                                                'mainCollegeApp.collegeRegistrationApp',
                                                'mainCollegeApp.coachingRegistrationApp'
    ]);

    collgeApp.controller('mainCollegeCtrl', function($rootScope){

    });

    collgeApp.config(function($httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';

        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    });

    })(angular);


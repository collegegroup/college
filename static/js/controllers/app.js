(function(angular){
    'use strict';

    var CRMApp = angular.module('mainCollegeApp', ['ui.router',
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

    CRMApp.controller('mainCollegeCtrl', function($rootScope){

    });

    })(angular);


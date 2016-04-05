(function(angular){
    'use strict';

    var CRMApp = angular.module('mainCollegeApp', ['ui.router',
                                                'mainCollegeApp.dashboard',
                                                'mainCollegeApp.addStateCityApp',
                                                'mainCollegeApp.subCityPincodeApp',
                                                'mainCollegeApp.viewLocationsApp',
                                                'mainCollegeApp.collegeManagementApp',
                                                'mainCollegeApp.coachingManagementApp'
    ]);

    CRMApp.controller('mainCollegeCtrl', function($rootScope){



    });

    })(angular);


(function(angular){
    'use strict';

    var collgeApp = angular.module('mainCollegeApp', ['ui.router', "ui.bootstrap",
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

    collgeApp.directive('focusMe', function($timeout) {
        return {
            scope: { trigger: '=focusMe' },
            link: function(scope, element) {
                scope.$watch('trigger', function(value) {
                    if(value === true) {
                        element[0].focus();
                        scope.trigger = false;
                    }
                });
            }
        };
    });


})(angular);


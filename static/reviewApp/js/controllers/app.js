(function(angular){
    'use strict';

    var collegeReviewApp = angular.module('collegeReviewApp', ['ui.router', "ui.bootstrap"
                                                
    ]);

    collegeReviewApp.controller('collegeReviewCtrl', function($rootScope){

    });

    collegeReviewApp.config(function($httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';

        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    });

    collegeReviewApp.directive('focusMe', function($timeout) {
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


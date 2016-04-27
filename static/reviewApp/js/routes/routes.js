/**
 * Created by bhanu on 5/4/16.
 */

var collegeReviewApp = angular.module('collegeReviewApp');

collegeReviewApp.config(function($locationProvider, $stateProvider, $urlRouterProvider) {

    //$locationProvider.html5Mode(true);

    $urlRouterProvider.otherwise('/review');

    console.log('Url params: ', window.location);

    $stateProvider

        .state('review home', {

            url: '/review',

            templateUrl: '/static/reviewApp/templates/ReviewSearch.html',

            controller: function() {

                alert('review home');

            }

        })

        .state('review college', {

            url: '/review/college',

            templateUrl: '/static/reviewApp/templates/ReviewSearch.html',

            controller: function() {

                alert('review/college');

            }

        });
            
            

    });

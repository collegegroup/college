/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingManagementApp', []);

app.controller('coachingManagementCtrl', function($scope, HTTPService, utilityService) {

    $scope.coachingCategories = [];

    $scope.coachingCategory = '';

    $scope.coachingCourse = '';

    /*
     * This for get coaching categories
     * */
    HTTPService.GETRequest('/category/coaching/', '', 'getCoachingCategories');
    /*
     * This for get coaching categories
     * */








    /*
     * This method is used to add coaching category
     * */
    $scope.addCoachingCategory = function(coachingCourse, coachingCategory) {

        var formData = utilityService.objectToRequestData({category_name: coachingCategory, course_name: coachingCourse});

        HTTPService.POSTRequest('/add/category/coaching/', formData, 'addCoachingCategory');

    };
    /*
     * This method is used to add coaching category
     * */








    /*
     * This is for get coaching categories response
     * */
    $scope.$on('addCoachingCategorySuccess', function (event, response) {

        console.log('addCoachingCategory: ', response);

    });
    $scope.$on('addCoachingCategoryError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */







    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getCoachingCategoriesSuccess', function (event, response) {

        $scope.coachingCategories = response.data.data.categories;

    });
    $scope.$on('getCoachingCategoriesError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});


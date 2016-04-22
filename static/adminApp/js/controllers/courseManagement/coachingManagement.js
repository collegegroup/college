/**
 * Created by bhanu on 5/4/16.
 */


var app = angular.module('mainCollegeApp.coachingManagementApp', []);

app.controller('coachingManagementCtrl', function($scope, HTTPService, utilityService) {

    $scope.coachingCategories = [];

    $scope.coachingCategoriesCourses = [];

    $scope.coachingCategory = '';

    $scope.coachingCourse = '';

    $scope.searchCoachingCategoriesCourses = '';

    /*
     * This for get coaching categories
     * */
    HTTPService.GETRequest('/category/coaching/', '', 'getCoachingCategories');
    /*
     * This for get coaching categories
     * */
    /*
     * This for get category course
     * */
    HTTPService.GETRequest('/category/course/coaching/', '', 'getCoachingCategoriesCourses');
    /*
     * This for get category course
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

        $scope.coachingCategoriesCourses.push({"course_name": $scope.coachingCourse, "category_name": $scope.coachingCategory});

        $scope.coachingCategory = '';

        $scope.coachingCourse = '';

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
    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getCoachingCategoriesCoursesSuccess', function (event, response) {

        console.log('coachingCategoriesCourses: ', response);

        $scope.coachingCategoriesCourses = response.data.data.categories_courses;

    });
    $scope.$on('getCoachingCategoriesCoursesError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});


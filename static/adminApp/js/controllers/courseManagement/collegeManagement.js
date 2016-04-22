
var app = angular.module('mainCollegeApp.collegeManagementApp', []);

app.controller('collegeManagementCtrl', function($scope, HTTPService, utilityService) {

    $scope.collegeCategories = [];

    $scope.collegeCategoriesCourses = [];

    $scope.collegeCategory = '';

    $scope.collegeCourse = '';

    $scope.searchCollegeCategoriesCourses = '';

    /*
    * This for get college categories
    * */
    HTTPService.GETRequest('/category/college/', '', 'getCollegeCategories');
    /*
    * This for get college categories
    * */
    /*
     * This for get category course
     * */
    HTTPService.GETRequest('/category/course/college/', '', 'getCollegeCategoriesCourses');
    /*
     * This for get category course
     * */








    /*
    * This method is used to add college category
    * */
    $scope.addCollegeCategory = function(collegeCourse, collegeCategory) {

        var formData = utilityService.objectToRequestData({category_name: collegeCategory, course_name: collegeCourse});

        HTTPService.POSTRequest('/add/category/college/', formData, 'addCollegeCategory');

    };
    /*
    * This method is used to add college category
    * */








    /*
     * This is for get college categories response
     * */
    $scope.$on('addCollegeCategorySuccess', function (event, response) {

       console.log('addCollegeCategory: ', response);

        $scope.collegeCategoriesCourses.push({"course_name": $scope.collegeCategory, "category_name": $scope.collegeCourse});

        $scope.collegeCategory = '';

        $scope.collegeCourse = '';

    });
    $scope.$on('addCollegeCategoryError', function (event, response) {

    });
    /*
     * This is for get college categories response
     * */







    /*
     * This is for get college categories response
     * */
    $scope.$on('getCollegeCategoriesSuccess', function (event, response) {

        $scope.collegeCategories = response.data.data.categories;

    });
    $scope.$on('getCollegeCategoriesError', function (event, response) {

    });
    /*
     * This is for get college categories response
     * */
    /*
     * This is for get coaching categories response
     * */
    $scope.$on('getCollegeCategoriesCoursesSuccess', function (event, response) {

        console.log('coachingCategoriesCourses: ', response);

        $scope.collegeCategoriesCourses = response.data.data.categories_courses;

    });
    $scope.$on('getCollegeCategoriesCoursesCoursesError', function (event, response) {

    });
    /*
     * This is for get coaching categories response
     * */

});
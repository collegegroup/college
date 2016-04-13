
var app = angular.module('mainCollegeApp.collegeManagementApp', []);

app.controller('collegeManagementCtrl', function($scope, HTTPService, utilityService) {

    $scope.collegeCategories = [];

    $scope.collegeCategory = '';

    $scope.collegeCourse = '';

    /*
    * This for get college categories
    * */
    HTTPService.GETRequest('/category/college/', '', 'getCollegeCategories');
    /*
    * This for get college categories
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

});
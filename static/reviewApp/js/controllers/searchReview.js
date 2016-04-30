/**
 * Created by bhanu on 26/4/16.
 */

var searchReviewApp = angular.module('mainCollegeApp.searchReview', ['MassAutoComplete']);

searchReviewApp.controller('searchReviewCtrl', function($scope, $rootScope, HTTPService, utilityService, $location) {

    $scope.searchQuery = '';

    $scope.selectedRecord = '';

    $scope.acadamies = '';


    function suggest_state(term) {
        var q = term.toLowerCase().trim();
        var results = [];

        // Find first 10 states that start with `term`.
        for (var i = 0; i < $scope.acadamies.length && results.length < 10; i++) {
            var acadamy = $scope.acadamies[i];
            if (acadamy.name.toLowerCase().indexOf(q) === 0)
                results.push(acadamy);
        }
        console.log(results);
        return results;
    }

    $scope.autocomplete_options = {
        suggest: suggest_state
    };

    $rootScope.setSelectedRecordData = function (selectedItem) {

        $scope.selectedRecord = selectedItem

    };


    /*
     * This for get all academy details
     * */
    $scope.getRecords = function (searchQuery) {

        if(searchQuery != '') {

            var formData = utilityService.objectToRequestData({name_prefix: searchQuery});

            HTTPService.POSTRequest('/review/search/', formData, 'getAllAcademyDetails');

        }

    };
    /*
     * This for get call all academy details
     * */







    /*
    * This methos is used to redirect the acadamy page
    * */
    $scope.goToAcadamyPage = function (selectedRecord) {

        console.log('selected record: ', selectedRecord);

        $location.path('/review/'+selectedRecord.type+'/'+selectedRecord.id);

    };
    /*
     * This methos is used to redirect the acadamy page
     * */







    /*
     * This is for get all academy details success response
     * */
    $scope.$on('getAllAcademyDetailsSuccess', function (event, response) {

        console.log('Response: ', response.data.data.academies);

        $scope.acadamies = response.data.data.academies;

    });
    $scope.$on('getAllAcademyDetailsError', function (event, response) {

    });
    /*
     * This is for get all academy details success response
     * */

});

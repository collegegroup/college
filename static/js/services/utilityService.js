/**
 * Created by bhanu on 8/4/16.
 */


(function(angular){
    'use strict';

    angular.module('mainCollegeApp')

        .factory('utilityService', ['$rootScope', function ($rootScope) {

            return {

                objectToRequestData: function(dataObj) {

                    var form_data = '';

                    for ( var key in dataObj ) {

                        form_data = form_data+key+'='+dataObj[key]+'&';

                    }

                    return form_data.slice(0, -1);

                }

            }

        }]);


})(angular);
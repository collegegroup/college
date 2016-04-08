/**
 * Created by bhanu on 8/4/16.
 */


(function(angular){
    'use strict';

    angular.module('mainCollegeApp')

        .factory('HTTPService', ['$rootScope', '$http', function ($rootScope, $http) {

            return {

                POSTRequest: function(URL, data) {

                    $http({

                        method: 'POST',

                        url: URL,

                        data:  data,

                        headers: {

                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

                        }

                    }).then(function successCallback(response) {

                        if(response.data.status == 'success'){



                        }



                    }, function errorCallback(response) {



                    });

                }

            }

        }]);


})(angular);

/**
 * Created by bhanu on 8/4/16.
 */


(function(angular){
    'use strict';

    angular.module('mainCollegeApp')

        .factory('HTTPService', ['$rootScope', '$http', function ($rootScope, $http) {

            return {

                POSTRequest: function(URL, data, emitMessage) {

                    $http({

                        method: 'POST',

                        url: URL,

                        data:  data,

                        headers: {

                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

                        }

                    }).then(function successCallback(response) {

                        if(response.data.status == 'success'){

                            $rootScope.$broadcast(emitMessage+"Success", response);

                        } else {

                            $rootScope.$broadcast(emitMessage+"Error", response);

                        }

                    }, function errorCallback(response) {

                        $rootScope.$broadcast(emitMessage+"Error", response);

                    });

                },

                GETRequest: function(URL, data, emitMessage) {

                    $http({

                        method: 'GET',

                        url: URL,

                        headers: {

                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

                        }

                    }).then(function successCallback(response) {

                        if(response.data.status == 'success'){

                            $rootScope.$broadcast(emitMessage+"Success", response);

                        } else {

                            $rootScope.$broadcast(emitMessage+"Error", response);

                        }

                    }, function errorCallback(response) {

                        $rootScope.$broadcast(emitMessage+"Error", response);

                    });

                }

            }

        }]);


})(angular);

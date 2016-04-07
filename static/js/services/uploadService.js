/**
 * Created by bhanu on 7/4/16.
 */


(function(angular){
    'use strict';

    angular.module('mainCollegeApp')

        .factory('uploadService', ['$rootScope', '$upload', function ($rootScope, $upload) {

            return {

                uploadFile : function(fileObj, uploadURL, uploadType, emitMessage) {

                    $rootScope.upload = $upload.upload({

                        url:  uploadURL,

                        data: {'uploadType': uploadType},

                        file: fileObj
                    
                    }).progress(function (evt) {

                        //parseInt(100.0 * evt.loaded / evt.total)

                    }).success(function (response){

                        $rootScope.$broadcast(emitMessage+" success", response);

                    }).error(function(response){

                        $rootScope.$broadcast(emitMessage+" error", response);

                    });

                }

            }

        }]);


})(angular);

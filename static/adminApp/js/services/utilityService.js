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

                },

                validateText : function(text, validateMessage) {

                    if (text) {

                        var text = text.toString();

                        if (text.trim().length == 0 || text == undefined) {

                            if(validateMessage != undefined) { console.log(validateMessage+' FAILED 1'); }

                            return false;

                        } else {

                            if(validateMessage != undefined) { console.log(validateMessage+' SUCCESS 1');}

                            return true;

                        }

                    } else {

                        if(validateMessage != undefined) { console.log(validateMessage+' FAILED 2'); }

                        return false;

                    }

                },

                validateNumber: function(number, validateMessage, min, max) {

                    if(number != undefined && number != ''){

                        if(typeof number === 'number') {

                            if(min == undefined || max == undefined) {

                                console.log(validateMessage + ' SUCCESS 1');

                                return true;

                            } else {

                                if (min <= number <= max) {

                                    console.log(validateMessage + ' SUCCESS 1');

                                    return true;

                                } else {

                                    console.log(validateMessage + ' FAILED 1');

                                    return false;

                                }

                            }

                        } else {

                            console.log(validateMessage+' FAILED 2');

                            return false;

                        }

                    } else {

                        console.log(validateMessage+' FAILED 3');

                        return false;

                    }



                },

                validateColorCode: function(colorCode, validateMessage) {

                    if(colorCode != '' && colorCode != undefined && colorCode != null && colorCode.trim().length != 0){

                        if(/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/.test(colorCode)){

                            console.log(validateMessage + ' SUCCESS 1');

                            return true;

                        }else{

                            console.log(validateMessage + ' FAILED 1');

                            return false;

                        }
                    }else{

                        console.log(validateMessage + ' FAILED 2');

                        return false;

                    }

                },

                validateEmail: function(emailVal, validateMessage) {

                    var regexp = (/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);

                    if (emailVal) {

                        if (emailVal.trim().length == 0 || emailVal == undefined) {

                            console.log(validateMessage+' FAILED 1');

                            return false;

                        } else {

                            if(regexp.test(emailVal)) {

                                console.log(validateMessage+" SUCCESS");

                                return true;

                            } else {

                                console.log(validateMessage+" FAILED2");

                                return false;

                            }

                        }

                    } else {

                        console.log(validateMessage+' FAILED 3');

                        return false;

                    }

                }

            }

        }]);


})(angular);
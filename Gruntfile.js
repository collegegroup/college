module.exports = function(grunt) {
    grunt.initConfig({ pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                mangle: false,/*{
                 except: ['jQuery', 'angular', 'exceptionLogService', 'printStackTrace']
                 },*/
                compress: {
                    drop_console: false  // <-
                }
            },
            production: {
                files: {
                    //'public/js/app/services.min.js': ['public/js/app/services/*.js'],
                    'static/adminApp/js/sourceMin/all.min.js': [
                        //'static/adminApp/js/controllers/app.js',
                        //'static/adminApp/js/routes/routes.js',

                        'static/adminApp/js/controllers/dashboard/dashboardCtrl.js',

                        'static/adminApp/js/controllers/location/addStateCityCtrl.js',
                        'static/adminApp/js/controllers/location/subCityPincodeCtrl.js',
                        'static/adminApp/js/controllers/location/viewLocationsCtrl.js',

                        'static/adminApp/js/controllers/courseManagement/collegeManagement.js',
                        'static/adminApp/js/controllers/courseManagement/coachingManagement.js',

                        'static/adminApp/js/controllers/instituteRegistration/schoolRegistration.js',
                        'static/adminApp/js/controllers/instituteRegistration/collegeRegistration.js',
                        'static/adminApp/js/controllers/instituteRegistration/coachingRegistration.js',

                        'static/adminApp/js/services/uploadService.js',
                        'static/adminApp/js/services/HTTPRequestService.js',
                        'static/adminApp/js/services/utilityService.js'

                    ],

                    'static/adminApp/js/sourceMin/cust.all.min.js': [
                        'static/js/lib/angular/angular-file-upload.min.js',
                        'static/js/lib/angular/angular-dateparser.min.js',
                        'static/js/lib/angular/angular-timepicker.min.js'

                    ]

                }
            },
            reviewAppMin: {
                files: {
                    'static/reviewApp/js/sourceMin/all.min.js': [
                        'static/reviewApp/js/directives/massautocomplete.js',
                        'static/reviewApp/js/directives/starRating.js',
                        
                        'static/reviewApp/js/controllers/searchReview.js',
                        'static/reviewApp/js/controllers/collegeReview.js',
                        'static/reviewApp/js/controllers/schoolReview.js',
                        'static/reviewApp/js/controllers/instituteReview.js'
                    ]
                }
            },
            mainLib: {
                files: {
                    'static/mainApp/sourceMin/cust.all.min.js': [
                        'static/js/lib/jquery/jquery.min.js',
                        'static/js/lib/jquery/jquery-ui.min.js',
                        'static/js/lib/angular/angular.min.js',
                        'static/js/lib/angular/angular-sanitize.min.js',
                        'static/js/lib/bootstrap/bootstrap.min.js',
                        'static/js/lib/bootstrap/ui-bootstrap-tpls.min.js',
                        'static/js/lib/angular/angular-ui-router.min.js'
                    ]
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-contrib-less");
    grunt.loadNpmTasks('grunt-contrib-compress');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-requirejs');

    grunt.registerTask("minify", ["uglify"]);

};
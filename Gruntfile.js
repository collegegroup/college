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
                    'static/js/sourceMin/all.min.js': [
                        'static/js/controllers/app.js',
                        'static/js/controllers/dashboardCtrl.js',
                        'static/js/controllers/location/addStateCityCtrl.js',
                        'static/js/controllers/location/subCityPincodeCtrl.js',
                        'static/js/controllers/location/viewLocationsCtrl.js'

                    ],

                    'static/js/sourceMin/cust.all.min.js': [
                        'static/js/lib/jquery/jquery.min.js',
                        'static/js/lib/jquery/jquery-ui.min.js',
                        'static/js/lib/bootstrap/bootstrap.min.js',
                        'static/js/lib/angular/angular.min.js',
                        'static/js/lib/angular/angular-route.min.js'
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
require.config({
    //By default load any module IDs from js/lib
    catchError: true,
    baseUrl: '/static/js',

    paths: {

    },

    waitSeconds: 7000

});
// Start the main app logic.
require(['/static/adminApp/js/sourceMin/cust.all.min.js'],function(){
    console.log('Loaded Admin lib files');
    require(['/static/adminApp/js/sourceMin/all.min.js', '/static/reviewApp/js/sourceMin/all.min.js'],function(){
        console.log("Loading Admin app...");
        angular.bootstrap(document.body, [
            'mainCollegeApp'
        ]);
        console.log('Loaded Admin source files');
    });
});


require.onError = function (err) {
    if (err.requireType == 'timeout' || err.requireType =='scripterror') {
        //window.location.reload();
        alert('An error occurred please refresh the page');
        throw err;
    } else {
        //window.location.reload();
        alert('An error occurred please refresh the page!');
        //window.location.reload();
        throw err;
    }
};
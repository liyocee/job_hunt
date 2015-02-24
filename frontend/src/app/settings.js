'use strict';
(function(){
    angular.module('jobHunt')
    .config(['$stateProvider','$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise( '/dashboard' );
        }])

    .config(['$httpProvider', function($httpProvider){
        $httpProvider.defaults.withCredentials = true;
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.common = {
            'Content-Type':'application/json'
        };
    }])

    .run(['$http','$cookies', function ($http, $cookies) {
        // apparently the angular doesn't do CSRF headers using
        // CORS across different domains thereby this hack
        var csrftoken = $cookies.csrftoken;
        var header_name = 'X-CSRFToken';
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.patch['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.common[header_name] = csrftoken;
        $.ajaxSetup({
            xhrFields: {
                withCredentials: true
            }
        });
    }]);

    /*.run(['authService', '$location',function(authService, $location){
        if(!authService.isLoggedIn()){
            $location.path('/login');
        }
    }])

    .run(["$rootScope", "$location", "authService",
        function($rootScope, $location, authService){
            $rootScope.$on("$stateChangeStart", function(){
                if(!authService.isLoggedIn()) {
                    $location.path("/login");
                }else{
                    $rootScope.current_user = authService.getUser();
                }
            });
        }]);*/
})();

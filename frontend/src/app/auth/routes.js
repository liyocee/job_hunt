'use strict';
(function(){
    angular.module('jobHunt.auth.routes', ['ui.router'])
        .config(['$stateProvider', function($stateProvider){
            $stateProvider
                .state('login', {
                    url: '/login',
                    controller: 'LoginController',
                    templateUrl: 'auth/tpls/login.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
                .state('logout', {
                    url: '/logout',
                    controller: 'LogoutController',
                    templateUrl: 'auth/tpls/login.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
        ;
        }]);

})();

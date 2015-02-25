"use strict";

(function(){
    angular.module("jobHunt.auth.controllers", [
        "jobHunt.common.providers",
        "jobHunt.auth.services"
    ])

    .controller("LoginController",[
        "$scope","$location","authService",
        function($scope, $location, authService){
            var user = {
                username: "",
                password: "",
                login_as: ""
            };
            $scope.user = user;
            $scope.login = function(){
                authService.login(user).success(function(data){
                    console.log($scope.user_type);
                    var user = {
                        "email": data.email,
                        "username": data.username,
                        "id": data.id
                    };
                    authService.saveUser(user);
                    var redirect_url = "";
                    if($scope.user.login_as === 'employer'){
                        redirect_url = "/#employer_dashboard";
                    }else{
                        redirect_url = "/#employee_dashboard";
                    }
                    window.location.href = redirect_url;
                }).error(function(err){
                    $scope.error = err.message;
                });

            };


        }
    ])

    .controller("LogoutController", [
        "$scope", "authService",
        function($scope,authService){
            authService.logout();
            window.location.href = "/#login";
            window.location.reload();

        }
    ]);
})();

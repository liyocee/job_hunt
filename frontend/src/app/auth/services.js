"use strict";
(function(){
        var login_url = "api/v1/auth/login/";
        var logout_url = "api/v1/auth/logout/";
        angular.module("jobHunt.auth.services", [
            "jobHunt.common.providers",
            "jobHunt.common.services"
        ])
        .service("authService", ["storageService", "api",
             function(storageService, api){
                var store_keys = {
                    user: "auth.user",
                    is_logged_in: "auth.status"
                };

                this.login = function(credentials){
                    return api.makeCall("POST", login_url, credentials);
                };

                this.saveUser = function(user){
                    storageService.setItem(store_keys.user, user);
                    storageService.setItem(store_keys.is_logged_in, true);
                    return;
                };

                this.getUser = function(){
                    return storageService.getItem(store_keys.user);
                };
                this.logout = function(){
                    storageService.removeItem(store_keys.user);
                    storageService.removeItem(store_keys.logged_in);
                    storageService.clear();
                    return api.makeCall("GET", logout_url);
                };

                this.isLoggedIn = function(){
                    var logged_in = storageService.getItem(store_keys.is_logged_in);
                    if(_.isNull(logged_in)){
                        return false;

                    }
                    return logged_in;
                };
            }]);
    })();

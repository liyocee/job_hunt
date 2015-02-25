"use strict";
(function(){
    angular.module("jobHunt",[
        "templates-app",
        "templates-common",
        "ui.router",
        "ui.bootstrap",
        "ngCookies",

        // my apps
        "jobHunt.config",
        "jobHunt.common",
        "jobHunt.auth",
        "jobHunt.employer"
    ]);
})();

'use strict';
(function(){
    var base_url = "api/v1/common/";
    angular.module('jobHunt.common.services', ["jobHunt.common.providers"])
    .service("storageService", [function() {
        this.getItem = function(key) {
            return JSON.parse(localStorage.getItem(key));
        };
        this.setItem = function(key, value) {
            localStorage.setItem(key, JSON.stringify(value));
        };
        this.removeItem = function(key) {
            localStorage.removeItem(key);
        };
        this.dumpScope = function (scope, location) {
            var dump = {
                location: location,
                scope: (_.isUndefined(scope.data) || _.isNull(scope.data)) ? {} : scope.data
            };
            this.setItem("dump", dump);
        };
        this.loadScope = function () {
            return this.getItem("dump");
        };

        this.clear = function() {
            localStorage.clear();
        };
    }])
    .service("commonService", ["api",
             function(api){
                this.getIndustries = function(){
                    return api.makeCall("GET", base_url+"industry/");
                };
                this.getSkills = function(){
                    return api.makeCall("GET", base_url+"skill/");
                };
                this.getLocations = function(){
                    return api.makeCall("GET", base_url+"location/");
                };

            }]);
})();

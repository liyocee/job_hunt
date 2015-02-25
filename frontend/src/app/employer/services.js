"use strict";
(function(){
        var url = "api/v1/employer/";
        var jobs_url = "api/v1/employer/jobs/";
        angular.module("jobHunt.employer.services", [
            "jobHunt.common.providers"
        ])
        .service("employerService", ["api",
             function(api){
                this.register = function(data){
                    return api.makeCall("POST", url, data);
                };
                this.getJobs = function(){
                    return api.makeCall("GET", jobs_url);
                };

                this.postJob = function(job){
                    return api.makeCall("POST", jobs_url, job);
                };
            }]);
    })();

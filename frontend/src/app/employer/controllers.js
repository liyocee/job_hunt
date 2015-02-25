"use strict";
(function(){
    angular.module("jobHunt.employer.controllers", [
        "jobHunt.employer.services",
        "jobHunt.auth.services",
        "jobHunt.common.services"
    ])
    .controller('EmployerDashboardController', ['$scope', 'employerService',
                function($scope, employerService){
                    $scope.where = 'employer';
                    employerService.getJobs($scope.data).success(
                            function(data){
                                $scope.jobs = data.results;
                            }).error(function(err){
                                console.log(err);
                            });

                }])
    .controller('EmployerRegisterController', ['$scope', 'employerService',
                function($scope, employerService){
                    $scope.register = function(){
                        employerService.register($scope.data).success(
                            function(data){
                                $scope.employer = data;
                            }).error(function(err){
                                console.log(err);
                            });
                    };

                }])
    .controller('EmployerPostJobController', ['$scope','$location', 'employerService',
                'authService',"commonService",
                function($scope,$location, employerService, authService, commonService){
                    $scope.job = {
                        job: {
                            "name": "",
                            "start_date": "",
                            "expires_on": "",
                            "industry": "",
                            "location": "",
                            "skills": ""
                        },
                        "employer": authService.getUser().id
                    };
                    commonService.getSkills().success(function(data){
                        $scope.skills = data.results;
                    });
                    commonService.getIndustries().success(function(data){
                        $scope.industries = data.results;
                    });
                    commonService.getLocations().success(function(data){
                        $scope.locations = data.results;
                    });
                    $scope.postJob = function(){
                        $scope.job.job.skills = [$scope.job.job.skills];
                        console.log($scope.job);
                        employerService.postJob($scope.job).success(
                            function(){
                                $location.path("/employer_job_list");
                            }).error(function(err){
                                console.log(err);
                            });
                    };

                }])
    .controller('EmployerJobListController', ['$scope', 'employerService',
                function($scope, employerService){
                    employerService.getJobs($scope.data).success(
                            function(data){
                                $scope.jobs = data.results;
                            }).error(function(err){
                                console.log(err);
                            });

                }]);
})();

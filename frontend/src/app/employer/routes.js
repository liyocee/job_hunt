'use strict';
(function(){
    angular.module('jobHunt.employer.routes', ['ui.router'])
        .config(['$stateProvider', function($stateProvider){
            $stateProvider
                .state('employer_dashboard', {
                    url: '/employer_dashboard',
                    controller: 'EmployerDashboardController',
                    templateUrl: 'employer/tpls/dashboard.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
                .state('employer_register', {
                    url: '/employer_register',
                    controller: 'EmployerRegisterController',
                    templateUrl: 'employer/tpls/register.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
                .state('employer_postjob', {
                    url: '/employer_postjob',
                    controller: 'EmployerPostJobController',
                    templateUrl: 'employer/tpls/post_job.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
                .state('employer_joblist', {
                    url: '/employer_job_list',
                    controller: 'EmployerJobListController',
                    templateUrl: 'employer/tpls/job_list.tpl.html',
                    data:{ pageTitle: 'Job Hunt' }
                })
        ;
        }]);

})();

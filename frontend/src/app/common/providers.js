"use strict";
(function(){
    angular.module("jobHunt.common.providers", [])
    .provider("api",function(){
        this.$get = ["$http", "SERVER_URL", function($http, SERVER_URL){
            return {
                api_url: SERVER_URL,
                makeCall: function(method, url, data){
                    var config = {};
                    config.data = data;
                    config.method = method;
                    config.url = this.joinUrl(url);
                    return $http(config);
                },
                joinUrl: function(uri_frag){
                  //strip off leading '/'
                    if(uri_frag[0]==='/'){
                        uri_frag = uri_frag.substr(1, uri_frag.length);
                    }
                    return this.api_url+uri_frag;
                }
            };
        }];
    });
})();

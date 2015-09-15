'use strict';

var app = angular.module("app", ["ngRoute"]);

app.constant('global', {
        host: "http://localhost:8888"
    }
);

app.config(function ($httpProvider, $routeProvider, $locationProvider, $interpolateProvider) {

    $interpolateProvider.startSymbol('{*');
    $interpolateProvider.endSymbol('*}');

    $httpProvider.defaults.transformRequest = function (obj) {
        var str = [];
        for (var p in obj) {
            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
        return str.join("&");
    };

    $httpProvider.defaults.headers.post = {
        'Content-Type': 'application/x-www-form-urlencoded'
    };

    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/welcome.html', {
            templateUrl: '/static/html/welcome.html'
        })
        .when('/audit.html', {
            templateUrl: '/static/html/audit.html'
        })
        .otherwise({
            redirectTo: '/welcome.html'
        });
});
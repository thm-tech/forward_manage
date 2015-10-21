'use strict';

var app = angular.module("app", ["ngRoute", "ivpusic.cookie"]);

app.constant('global', {
        host: "http://localhost:8888"
    }
);

app.config(function ($httpProvider, $routeProvider, $locationProvider, $interpolateProvider) {

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
        .when('/index.html', {
            templateUrl: '/static/html/welcome.html'
        })
        .when('/audit.html', {
            templateUrl: '/static/html/audit.html'
        })
        .when('/feedback.html', {
            templateUrl: '/static/html/feedback.html'
        })
        .when('/documents.html', {
            templateUrl: '/static/html/documents.html'
        })
        .when('/login.html', {
            templateUrl: '/static/html/login.html'
        })
        .otherwise({
            redirectTo: '/index.html'
        });
});

app.run(['$rootScope', '$location', 'ipCookie', function ($rootScope, $location, ipCookie) {
    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        if (!ipCookie('id')) {
            // There are two ways to implementation route/cookies controll
            // First way is use event.proventDefault(), like thus
            // event.preventDefault();
            // Here is the second way
            $location.path('/login.html')
        }
    })
}]);
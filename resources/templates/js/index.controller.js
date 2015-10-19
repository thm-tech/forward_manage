'use strict';

app.controller("index", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {

        $scope.navbar = {};
        $scope.navbar.index = 1;

        var clickNav = $scope.clickNav = function(index){
            $scope.navbar.index = index;
        };

        var logout = $scope.logout = function(){
            $http.post('/logout').success(function(data){
                if(data.is_success){
                    $location.path('/login.html')
                }
            })
        };

    }]
);
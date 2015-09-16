'use strict';

app.controller("welcome", ['$scope', '$http', 'global', function ($scope, $http, global) {

        $scope.name = 'hh';

        var getLike = $scope.getLike = function () {
            $http({
                url: global.host + '/zan',
                method: 'GET'
            }).success(function (data) {
                $scope.islike = data.is_zan;
            });
        };
        getLike();

        var addLike = $scope.addLike = function () {
            $http({
                url: global.host + '/zan',
                method: 'POST'
            }).success(function (data) {
            });
        };

        var deleteLike = $scope.deleteLike = function () {
            $http({
                url: global.host + '/zan',
                method: 'delete'
            }).success(function (data) {
            });
        };

        $scope.like = function () {
            $scope.islike = !$scope.islike;
            if($scope.islike){
                addLike()
            }else {
                deleteLike()
            }
        }

    }]
);
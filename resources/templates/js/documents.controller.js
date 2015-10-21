/**
 * Created by Mohanson on 2015/10/14.
 */
'use strict';

app.controller("documents", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {

        var init = $scope.init = function () {
            $http({
                url: '/documents',
                method: 'GET'
            }).success(function (data) {
                $scope.documents = data.documents;
            })
        };
        init();

    }]
);
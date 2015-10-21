/**
 * Created by Mohanson on 2015/9/16.
 */
'use strict';

app.controller("audit", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {

        var init = $scope.init = function () {
            $http({
                url: '/audit/waits',
                method: 'GET'
            }).success(function (data) {
                $scope.auditWaits = {};
                $scope.auditWaits.totalNum = data.total_num;
                $scope.auditWaits.shops = data.shops;
            })
        };
        init();

        var auditPass = $scope.auditPass = function (shop_id) {
            $http({
                url: '/audit/' + String(shop_id) + '/pass',
                method: 'PUT'
            }).success(function (data) {
                if (data.is_success == true) {
                    init();
                } else {
                    alert('something wrong!')
                }
            })
        };

        var notAuditPass = $scope.notAuditPass = function (shop_id) {
            $http({
                url: '/audit/' + String(shop_id) + '/notpass',
                method: 'PUT'
            }).success(function (data) {
                if (data.is_success == true) {
                    init();
                } else {
                    alert('something wrong!')
                }
            })
        };


    }]
);
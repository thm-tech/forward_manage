/**
 * Created by Mohanson on 2015/9/16.
 */
'use strict';

app.controller("audit", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {

        $scope.auditLists = {};

        var getAuditWaits = $scope.getAuditWaits = function(){
            $http({
                url: '/audit/waits',
                method: 'GET'
            }).success(function (data) {
                $scope.auditLists.totalNum = data.total_num;
                $scope.auditLists.shops = data.shops;
            })
        };

        var getNotPassAudit = $scope.getNotPassAudit = function(){
            $http.get('/audit/notpassed').success(function(data){
                //$scope.auditLists = {};
                //$scope.auditLists.totalNum = data.total_num;
                $scope.auditLists.shops = data.shops;
            })
        };

        var init = $scope.init = function () {
            getAuditWaits();
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

        $scope.navIndex = 1;
        var changeNav = $scope.changeNav = function(index){
            $scope.navIndex = index;
        };



    }]
);
'use strict';

app.controller("index", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {

        // circle progress
        //var windowHeight = $(window).height();
        //$(window).bind("scroll", function () {
        //    var recentScroll = $(window).scrollTop();
        //    $scope.percent = (recentScroll + 30 - 2 * windowHeight) * 100 / windowHeight;
        //    if ($scope.percent < 0) {
        //        $scope.percent = 0;
        //    } else {
        //        if ($scope.percent > 75) {
        //            $scope.percent = 75;
        //        } else {
        //            $scope.percent = parseInt($scope.percent);
        //        }
        //    }
        //    $scope.$digest();
        //});
        //
        //
        //var slideLeft = function(boardid){
        //    $("#" + boardid + " div").css({"width": "0", "left": "0", "right": "auto"});
        //};
        //
        //var slideRight = function(boardid){
        //    $("#" + boardid + " div").css({"width": "0", "right": "0", "left": "auto"});
        //};
        //
        //// bar
        //var before_board = "idbord1";
        //$('#idNavBar').on('activate.bs.scrollspy', function () {
        //    var current_borad = $('li.active').attr('id');
        //    var next_board = before_board.slice(0, 6) + String(parseInt(before_board.slice(6, 7)) - 1);
        //    if (current_borad > before_board) {
        //        $("#" + before_board + " div").css({"width": "0", "right": "0", "left": "auto"});
        //        $("#" + current_borad + " div").css({"width": "100%", "left": "0", "right": "auto"});
        //    } else if(current_borad < before_board){
        //        $("#" + before_board + " div").css({"width": "0", "left": "0", "right": "auto"});
        //        $("#" + current_borad + " div").css({"width": "100%", "right": "0", "left": "auto"});
        //    }else {
        //
        //    }
        //    before_board = current_borad;
        //})

    }]
);
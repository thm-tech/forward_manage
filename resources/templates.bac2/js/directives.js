/**
 * Created by Mohanson on 2015/7/11.
 * restrict: "EACM",元素, 属性, 样式, 注释
 */
app.directive("magNav", ["$rootScope", "$location", function ($rootScope, $location) {
    return {
        restrict: "A",
        link: function (scope, element, attrs) {
            var navHeight = -1;
            navHeight = $(window).height() - element.height();

            $(window).bind("scroll", function () {
                if ($(window).scrollTop() > navHeight) {
                    element.addClass("nav-fixed");
                }
                else {
                    element.removeClass("nav-fixed");
                }
            });
        }
    }
}]);

app.directive("showpath", ["$rootScope", "$location", function ($rootScope, $location) {
    return {
        restrict: "A",
        link: function (scope, element, attrs) {
            var shouldShow = function () {
                if ($location.path() == attrs.showpath) {
                    element.css({"visibility": "visible", "display": "block"});
                } else {
                    element.css({"visibility": "hidden", "display": "none"});
                }
            };
            shouldShow();
            $rootScope.$on("$locationChangeSuccess", function () {
                shouldShow()
            });
        }
    }
}]);

app.directive("scrollHide", [function () {
    return {
        restrict: "A",
        scope: true,
        link: function (scope, element, attrs) {
            var windowHeight = $(window).height();
            $(window).bind("scroll", function () {
                var recentScroll = $(window).scrollTop();
                var percent = (recentScroll - windowHeight * (parseInt(attrs.scrollHide) - 1)) / parseInt(windowHeight);
                var newPercent = 0;
                if (percent < 1) {
                    newPercent = 1 - percent;
                    if (newPercent < 0.2) {
                        newPercent = 0.2;
                    }
                } else {
                    if (percent < 0) {
                        newPercent = 1;
                    }
                }
                element.css({'opacity': newPercent});
            });
        }
    }
}]);

app.directive("circleProgress", [function () {
    return {
        restrict: "AE",
        replace: 'true',
        transclude: true,
        template: '<div class="circle-progress"><div class="pie_left"><div class="left"></div></div><div class="pie_right"><div class="right"></div></div><div class="mask"><span ng-transclude></span>%</div></div>',
        link: function (scope, element, attrs) {
            $(window).bind("scroll", function (index, el) {
                var num = element.find('span > span').text() * 3.6;
                if (num <= 180) {
                    element.find('.right').css('transform', "rotate(" + num + "deg)");
                    element.find('.left').css('transform', "rotate(0deg)");
                } else {
                    element.find('.right').css('transform', "rotate(180deg)");
                    element.find('.left').css('transform', "rotate(" + (num - 180) + "deg)");
                }
            });
        }
    }
}]);

//app.directive("scrollProgressContainer", [function () {
//    return {
//        restrict: "A",
//        scope: false,
//        link: function (scope, element, attrs) {
//            var windowHeight = $(window).height();
//            $(window).bind("scroll", function () {
//                var recentScroll = $(window).scrollTop();
//                scope.percent = (recentScroll - 2 * windowHeight) * 100 / windowHeight;
//                if(scope.percent < 0){
//                    scope.percent = 0;
//                }else {
//                    if(scope.percent > 100){
//                        scope.percent = 100;
//                    }
//                }
//                console.log(scope.percent);
//            })
//        }
//    }
//}]);

//app.directive("scrollHide", [function () {
//    return {
//        restrict: "A",
//        scope: {
//            scrollHide: "="
//        },
//        link: function (scope, element, attrs) {
//            //var windowHeight = $(window).height();
//            //$(window).bind("scroll", function () {
//                //var recentScroll = $(window).scrollTop();
//                //var percent = recentScroll / (windowHeight * parseInt(scope.scrollHide));
//                //element.css({'opacity': 1 - percent})
//            //});
//        }
//    }
//}]);

//app.directive("alert", [function () {
//    return {
//        restrict: "A",
//        scope: {
//            what: '='
//        },
//        link: function (scope, element, attrs) {
//            element.bind("click", function () {
//                console.log(attrs.alert)
//            });
//        }
//    }
//}]);
//
//
////
//app.directive("addBookButton", ['Book',
//    function (Book) {
//        return {
//            restrict: "A",
//            link: function (scope, element, attrs) {
//                element.bind("click", function () {
//                    Book.addBook({
//                        title: "Star Wars",
//                        author: "George Lucas"
//                    });
//                });
//            }
//        }
//    }]);
//
//// 替换
//app.directive('hello', function () {
//    return {
//        restrict: 'E',
//        template: '<div>Hi there</div>',
//        replace: true
//    };
//});
//
//// 高级替换(保留内容)
//app.directive('hello2', function () {
//    return {
//        restrict: 'E',
//        template: '<div>Hi there <span ng-transclude></span></div>',
//        transclude: true,
//        replace: true
//    };
//});
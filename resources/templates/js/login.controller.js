/**
 * Created by Mohanson on 2015/10/19.
 */
app.controller("login", ['$scope', '$http', '$location', function ($scope, $http, $location) {

        var login = $scope.login = function (user, pwd, remember) {
            var rem = 0;
            if (remember) {
                rem = 1
            }

            $http.post('/login', {
                'user': user,
                'pwd': pwd,
                'remember': rem
            }).success(function (data) {
                if (data.is_success) {
                    $location.path('/index.html')
                } else {
                    alert('user or pwd error!')
                }
            });
        }
    }]
);
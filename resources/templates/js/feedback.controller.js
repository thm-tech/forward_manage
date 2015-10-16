/**
 * Created by Mohanson on 2015/10/16.
 */
app.controller("feedback", ['$scope', '$http', '$location', 'global', function ($scope, $http, $location, global) {


        $scope.feedbacks = [];
        $scope.noMorefeedbacks = false;
        // 一次读取多少条数据
        var limit = 20;
        var offset = 0;
        // 用户点击 details 时, 将相关信息传入.
        $scope.detail = {};


        // 分页查询用户的所有反馈
        var getMoreFeedbackInofs = $scope.getMoreFeedbackInofs = function () {
            $http.get('/feedbacks/user', {
                params: {
                    'offset': offset,
                    'limit': limit
                }
            }).success(function (data) {
                if (data.feedback_infos.length < limit) {
                    $scope.noMorefeedbacks = true;
                } else {
                    offset += limit;
                }
                $scope.feedbacks = $scope.feedbacks.concat(data.feedback_infos);
            });

        };
        getMoreFeedbackInofs();

        // 当点击 detail 时, 触发
        var insertDetail = $scope.insertDetail = function (user_id, content) {
            $scope.detail.user_id = user_id;
            $scope.detail.content = content;
            getHistory(user_id);
        };

        // 取得平台和用户的聊天记录
        var getHistory = $scope.getHistory = function (user_id) {
            $http.get('/feedbacks/platform', {
                params: {
                    'user_id': user_id
                }
            }).success(function (data) {
                $scope.detail.history = data.feedback_infos;
            })
        };

        // 平台回复用户
        var sendFeedbackToUser = $scope.sendFeedbackToUser = function (user_id, content) {
            if ($scope.detail.platformFeedbackInfo) {
                $http.post('/feedbacks/platform', {
                    'user_id': user_id,
                    'content': content
                }).success(function (data) {
                    $scope.detail.platformFeedbackInfo = "";
                    getHistory(user_id);
                })
            }
        }

    }]
);
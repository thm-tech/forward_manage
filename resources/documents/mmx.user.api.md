# MMX.User.Api -- version 1
**Author: 尹吉林, 叶万标**
## /user/login

    post: //用户登陆
        {
            "mode":  //登录方式:1-账号登录，2-手机登录，3-邮箱登录
            ,"type":    //用户类型 type=4
            ,"account":  //账号
            ,"email": //邮箱，暂不支持邮箱登录
            ,"phone":  //手机号码
            ,"password":    //密码
            ,"dev": //登录设备，如为手机则为IMEI，如为web端登录则为IP地址
        }
        response: 
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"accID":  //账号ID
            ,"dev": //上次登录设备，如为手机则为IMEI，如为web端登录则为IP地址
        }

    
    post: //第三方登陆
        {
            "mode":  //登录方式:4-QQ登录，5-微信登录，6-微博登录，7-支付宝登录
            ,"type":    //用户类型 type=4
            ,"openID": //第三方账号系统用户唯一标识
            ,"dev": //上次登录设备，如为手机则为IMEI
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"accID":  //账号ID
            ,"isReg":   //是否是注册，即是否是第一次登录,0-非注册，1-是注册即第一次登录
            ,"dev": //上次登录设备，如为手机则为IMEI，如为web端登录则为IP地址
        }
        
## /user/logout
     post: //用户登出
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
        

## /user/register
    post: //用户注册
        {
            "phone":  //手机号码
            ,"password":    //密码
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"accID": //账号ID
        }
        
## /user/gencode
    post: //给指定手机发送验证码
        {
           "phone":  //手机号码
        }
        response:
       {                    
            "err":	//0-成功，其他为失败对应的错误码
       }
        
## /user/vercode
    post: //验证手机验证码
        {
            "phone":  //手机号码
            ,"code": //手机验证码
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }

## /user/resetpw
    post: //重置密码
        {
            "phone":  //手机号码
            ,"password": //新密码，须加密
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
        
## /user/personal
    get: //查询个人信息
        response:
            {                    
                "err":	//0-成功，其他为失败对应的错误码
                ,"info":    //用户信息
                    {
                        "name":    //用户名（昵称）
                        ,"portrait":    //头像URL
                        ,"gender":  //性别，1-男，2-女
                        ,"city":    //常居地城市ID
                        ,"phone": //绑定的手机号，为字符串
                        ,"mcode":   //喵喵号   
                        ,"qcode":   //二维码名片
                    }
            }
    post: //修改个人信息
        {
            "attr":   //个人信息属性ID，1-用户名，2-头像，3-性别，4-常居地
            ,"name":    //用户名（昵称）
            ,"portrait":    //头像URL
            ,"gender":  //性别，1-男，2-女
            ,"city":    //常居地城市ID
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
        

## /user/address
    get: //查询用户地址信息
        response:
            {                    
                "err":	//0-成功，其他为失败对应的错误码
                ,"addressList":    //地址信息列表
                    [
                        {
                            "addrID":   //地址索引
                            ,"name":    //联系人姓名
                            ,"phone":   //联系人手机
                            ,"address": //具体地址
                            ,"postcode":    //邮编
                            ,"default": //是否默认地址
                        },
                        ...
                    ]                       
            }
        }
    post: //修改用户地址信息
        {
            "addrID":   //地址索引
            ,"name":    //联系人姓名
            ,"phone":   //联系人手机
            ,"address": //具体地址
            ,"postcode":    //邮编
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
    put: //新增用户地址信息(当用户地址信息达到4个时, 禁止再新增地址)
        {
            "name":    //联系人姓名
            ,"phone":   //联系人手机
            ,"address": //具体地址
            ,"postcode":    //邮编
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"addrID":   //地址索引
        }
    delete: //删除用户地址信息, 当删除地址时，如果删除的地址为用户默认地址，则客户端指定剩下地址中的第一个（或id最大的那个）作为默认地址，
            //并由前端调用 "/user/address/default" 更改默认地址协议修改后台数据
        request:
        {
            "addrID":   //地址索引
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
        
## /user/address/default
    post: //设置用户默认地址
    {
        "addrID":   //地址索引
    }
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
    }
               
## /user/bindphone
    post: //绑定用户手机号
    {
        "phone":   //绑定手机
    }
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
    }
    
## /user/category
    get: //查询商品类别
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"categoryList":    //商店列表
            [
                {
                    "id":    //类别ID
                    ,"name":    //类别名称
                    ,"pic":  //类别图片
                    ,"child": //子类别列表
                        [
                            {
                                "id":    //类别ID
                                ,"name":    //类别名称
                                ,"pic":  //类别图片
                            },
                            ...
                        ]
                },
                ...
            ]
    }
    
## /user/shop/recommend?city=1
    get: //查询推荐品牌
    response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":    //商店列表
                {
                    "id":    //商店ID
                    ,"name":    //商店名称
                    ,"pic":  //商店图片
                    ,"dec":	//推荐词
                }
        }
        
## /user/shop?category=11&city=1&long=12&lat=33&offset=11&count=5
    get: //分类分页查询商店信息
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"shopList":    //商店列表
            [
                {
                    "id":    //商店ID
                    ,"name":    //商店名称
                    ,"picList":  //商店图片列表
                    ,"distance":    //离用户当前位置的距离，单位为km
                    ,"fans":    //粉丝数
                    ,"customers":   //当前正在该店逛的客户数
                },
                ...
            ]
    }
    
## /user/shop/name?sid=115
    get: //通过商店id查询商店名称
    response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopName":    //商店名称
        }
        
## /user/shop/enter?sid=11
    post: //访问商店.用户进入商店时, 需触发此请求
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
    }
    
## /user/shop/exit?sid=11
    post: //退出商店.用户退出商店时, 需触发此请求
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
    }
    
## /user/shop/customer?sid=11
    get: //查询商店当前逛店客户数
         //当用户进入某个商店后,启动定时器，每隔3分钟查询一次商店当前逛店客户数，当用户退出该商店，关闭定时器
    response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"count":   //当前逛店客户数
        }
        
## /user/goods?sid=2&offset=0&count=5
    get: //分页查询某商店商品
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"goodsList":    //商品列表
            [
                {
                    "id":   //商品ID
                    ,"price":   //原价
                    ,"promot":  //促销价
                    ,"pic": //商品图片  
                    ,"time":    //商品发布时间，发布时间与浏览时间在一周内的，打上新品标签
                },
                ...
            ]
    }
    
## /user/shop/activity?sid=1
    get: //查询商店有效活动
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"actList":    //特惠活动信息列表
            [
                {
                    "id":   //活动ID
                    ,"title":   //活动标题
                    ,"content":  //活动内容
                    ,"bt":"2015-01-01"  //有效期开始日期
                    ,"et":"2015-01-31"    //有效期截止日期
                },
                ...
            ]
    }
        
## /user/shop/info?sid=1
    get: //查询商店信息
    "response":
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"info":    //商店信息
            {
                "id":    //商店ID
                ,"name":    //商店名称，不需查询，在分页查询商定时已查询                            
                //,"distance":    //离用户当前位置的距离，单位为km，不需查询，在分页查询商定时已查询
                ,"fans":    //粉丝数，不需查询，在分页查询商定时已查询
                ,"customers":   //当前正在该店逛的客户数，不需查询，在分页查询商定时已查询
                ,"isFans": //是否粉丝，不需查询，本地数据库有记录所有粉丝店，查询本地数据库
                ,"picList":  //商店图片列表，不需查询，在分页查询商定时已查询                            
                ,"address": //商店地址
                ,"long":    //经度
                ,"lat": //维度
                ,"hours":   //营业时间
                ,"phone":   //服务电话
                ,"intro":   //商店介绍
            }
    }
    
## /user/goods/info?gid=1&barcode=xd124784
    get: //查询商品信息
    response:
    {                    
        "err":	//0-成功，其他为失败对应的错误码
        ,"info":    //商品信息
            {
                "id":    //商品ID
                "shop_id": //商店ID
                ,"desp":   //描述
                //,"is_favorite": //是否收藏品，不需查询，本地数据库有记载所有收藏商品记录，查询本地数据库
                ,"price":   //原价
                ,"promot":  //促销价
                ,"picList": //商品图片URL列表
                ,"basic":   //商品基本信息JSON，须解析后展现
                    [
                        {
                            "key":  //基本信息项的键，如“款式”
                            ,"value":   //基本信息项的值，如对应的款式“瘦身 宽松”
                        },
                        ...
                    ]
            }
    }
    
##　/user/goods/fit?gid=1&offset=0&count=5
    get:　//分页查询商品客户试穿图片　
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"picList":    //商品图片URL列表                       
        }
    
    put:　//增加商品客户试穿图片
        {
            "goodsID":    //商品ID
            ,"picURL":   //图片URL
            ,"description": //描述
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
    
## /user/shop/visit?time=1465589785&direct=1&count=5
    get: //分页查询逛过的店
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":
                [
                    {
                        "id":    //商店ID
                        ,"name":    //商店名称
                        ,"time":    //访问时间
                    } ,
                    ...
                ]                                       
        }
        
## /user/activity?city=1&offset=0&count=5
    get: //分页查询活动
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"actList":    //特惠活动信息列表
                [
                    {
                        "actID":   //活动ID                                
                        ,"title":   //活动标题
                        ,"content":  //活动内容
                        ,"bt":"2015-01-01"  //有效期开始日期
                        ,"et":"2015-01-31"    //有效期截止日期
                        ,"shopID":  //商店ID
                        ,"shopName":    //商店名称
                        ,"shopPic": //商店图片
                    },
                    ...
                ]
        }
        
## /user/shop/search?name=shopname&city=1&long=12&lat=33&offset=11&count=5
    get: //搜索商店
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":    //商店列表
                [
                    {
                        "id":    //商店ID
                        ,"name":    //商店名称
                        ,"picList":  //商店图片列表
                        ,"distance":    //离用户当前位置的距离，单位为km
                        ,"fans":    //粉丝数
                        ,"customers":   //当前正在该店逛的客户数
                    },
                    ...
                ]
        }
        
## /userweb/activity/1256
    get: //通过活动 id 查询活动详情
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"actID":   //活动ID                                
            ,"title":   //活动标题
            ,"content":  //活动内容
            ,"bt":"2015-01-01"  //有效期开始日期
            ,"et":"2015-01-31"    //有效期截止日期
            ,"shopID":  //商店ID
            ,"shopName":    //商店名称
            ,"shopPic": //商店图片
        }
        
## /user/friend/diff
    post: //查询本地存储的好友和后台好友的差异
        {
            "frdIDs": [] //本地保存的好友用户ID列表
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"addFrdIDs": []   //需要添加的好友用户ID列表
            ,"delFrdIDs": []   //需要删除的好友用户ID列表                        
        }
        
## /user/friend?uid=1&uid=2
    get: //查询好友信息
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"frdList":    //好友信息列表
                [
                    {
                        "frdID":    //好友ID
                        ,"rmkName": //好友备注名称
                        ,"nickName":    //好友昵称
                        ,"mcode":   //喵喵号
                        ,"portrait":    //头像URL
                    },
                    ...
                ]
        }
        
## /user/friend/name 
    post: //修改好友备注名
        {
            "frdID": //好友用户ID
            ,"rmkName": //好友备注名称
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                  
        }
        
## /user/friend/private?uid=1
    get: //查询好友隐私设置
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"setting":
                {
                    "favoriteEnable":    //好友的收藏是否可见，0-不可见，1-可见
                    ,"fansEnable":    //好友的粉丝店是否可见，0-不可见，1-可见
                    ,"visitEnable":    //好友的逛店历史是否可见，0-不可见，1-可见
                }                                       
        }
    
    
## /user/friend/favorite?uid=1&offset=0&count=5
    get: //分页查询好友收藏
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"goodsList":
                [
                    {
                        "id":    //商品ID
                        ,"desc":    //商品描述
                        ,"price":   //售价
                        ,"promot":  //促销价
                        ,"pic": //商品图片
                    } ,
                    ...
                ]                                       
        }
        
## /user/friend/fans?uid=1&offset=0&count=5
    get: //分页查询好友的粉丝店
       response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":
                [
                    {
                        "id":    //商店ID
                        ,"name":    //商店名称
                        ,"hasAct":   //有活动，有效活动
                        ,"hasNew":  //有新品上架，居查询时间一周以内
                        ,"pic": //商店图片
                    } ,
                    ...
                ]                                       
        }
        
## /user/friend/visit?uid=1&offset=0&count=5
    get: //分页查询好友逛过的商店
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":
                [
                    {
                        "id":    //商店ID
                        ,"name":    //商店名称
                        ,"pic": //商店图片
                        ,"time":    //逛店时间
                    } ,
                    ...
                ]                                       
        }
        
## /user/friend/invite
    post: //邀请加为好友
        {
            "mode": //添加方式，1-手机号，2-喵喵号，3-用户ID
            ,"phone": //手机号
            ,"mcode":   //喵喵号
            ,"userID":  //用户ID
            ,"remark":  //备注，为让好友知晓是谁，如我是某某
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                  
        }
        
## /user/friend/accept?uid=1
    post: //接受成为好友
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                  
        }
        
## /user/info?uid=10040&uid=10041
    get: //查询用户信息
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"userList":
                [
                    {
                        "userID":    //用户ID
                        ,"nickName":    //用户昵称
                        ,"city":   //城市名称
                        ,"portrait":    //头像URL
                    } ,
                    ...
                ]                                                          
        }
        

## /user/ffv/count?uid=10040
    get: //查询用户粉丝店、收藏商品、逛过店数量信息
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"ffvCount":
                {
                    "fans":    //粉丝店数量
                    ,"favorite":    //收藏商品数量
                    ,"visited":    //逛过的店数量 
                }                                                                            
        }

## /user/fans/diff
    post: //查询本地存储的粉店和后台的差异
        {
            "shopIDs": [] //本地保存的粉丝店ID列表
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"addShopIDs": []   //需要添加的粉丝店ID列表
            ,"delShopIDs": []   //需要删除的粉丝店ID列表                        
        }

## /user/fans/info?sid=1&sid=2
    get: //查询粉丝店信息
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":    //商店列表
                [
                    {
                        "id":    //商店ID
                        ,"name":    //商店名称 
                        ,"pic":  //商店图片                            
                        ,"time": //加粉丝时间
                        ,"msgEnable":   //是否允许推送消息
                    },
                    ...
                ]                       
        }

## /user/fans/news?sid=1&sid=2
    get: //查询是否有有效活动和新品上架
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"shopList":  //商店列表
                [
                    {
                        "id":   //商店ID
                        ,"hasAct":  //是否有有效活动，0-无，1-有
                        ,"hasNew":  //是否有新品，一周以内上架的商品，0-无，1-有
                    },
                    ...
                ]
        }

## /user/shop/concern?sid=1
    post: //关注商店
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
    delete: //取消关注商店
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
     
## /user/favorite/diff
    post: //查询本地存储的收藏和后台的差异
        request:
        {
            "goodsIDs": [] //本地保存的粉丝店ID列表
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"addGoodsIDs": []   //需要添加的收藏品ID列表
            ,"delGoodsIDs": []   //需要删除的收藏品ID列表                        
        }

## /user/favorite/info?gid=1&gid=2
    get: //查询收藏品信息
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"goodsList":    //商品列表
                [
                    {
                        "gid":    //商品ID
                        ,"sid": //商店ID
                        ,"desp":    //商品描述
                        ,"price":    //商品价格 
                        ,"promot":  //商品促销价格                           
                        ,"pic": //商品图片
                    },
                    ...
                ]                       
        }

## /user/goods/concern?gid=1
    post: //收藏商品
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
    delete: //取消收藏商品
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
        }
     
## /user/goods/promot?gid=1&gid=2
    get: //查询商品促销价
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"goodsList":    //商品列表
                [
                    {
                        "gid":    //商品ID
                        ,"promot":  //商品促销价格                           
                    },
                    ...
                ]                       
        }

## /user/goods/promot?gid=1&gid=2
    get: //查询收藏商品的最新信息
        response:
            {                    
                "err":	//0-成功，其他为失败对应的错误码
                ,"goodsList":    //商品列表
                    [
                        {
                            "gid":    //商品ID
                            ,"promot":  //商品促销价格 
                            ,"status":	//状态，如果是下架或删除，则收藏商品上显示下架水印图标
                        },
                        ...
                    ]                       
            }

## /user/city
    get: //查询平台支持的城市
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"cityList":    //平台支持的城市列表
                [
                    {
                        "id":    //城市ID
                        ,"name":  //城市名称                           
                    },
                    ...
                ]                       
        }

## /user/setting/private
    get: //获取隐私设置
        "response":
        {
            "err":	//0-成功，其他为失败对应的错误码 
            "setting":  
                {
                    "favoriteEnable":  //收藏是否对好友可见，0-不可见，1-可见
                    ,"fansEnable":    //粉丝店是否对好友可见，0-不可见，1-可见
                    ,"visitEnable":    //逛店历史是否对好友可见，0-不可见，1-可见
                }
        }
    post: //修改隐私设置
        {
            "favoriteEnable":  //收藏是否对好友可见，0-不可见，1-可见
            ,"fansEnable":    //粉丝店是否对好友可见，0-不可见，1-可见
            ,"visitEnable":    //逛店历史是否对好友可见，0-不可见，1-可见
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                
        }

## /user/setting/message
    post: //消息设置
        {
            "shopID":  //商店ID,-1表示针对所有粉丝店
            ,"msgEnable":    //是否接收消息，0-不接收，2-接收
        }
        
       response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                
        }

## /user/feedback?offset=0&count=10
    get: //获取用户反馈
        response:
            {                    
                "err":	//0-成功，其他为失败对应的错误码    
                "feedList":
                    [
                        {
                            "content":  //内容
                            ,"time":    //时间
                            ,"direction":   //方向，1-用户发送，2-发送给用户
                        },
                        ...
                    ]
            }
    post: //用户反馈
        {
            "feedback":  //用户反馈
        }
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码                
        }

## /user/version?sys=1
    get: //查询最新版本
        response:
        {                    
            "err":	//0-成功，其他为失败对应的错误码
            ,"version":    //最新版本号  
            ,"time":    //版本时间
            ,"remark":  //版本备注
            ,"packet":  //安装路径
        }
        
# MMX.User.Api -- version 2
**Author: 叶万标**

## /userweb/(\w+)/friends
    get: //获取按照首字母分类的用户好友列表
        response: {'total_num': 1,
         'friends': {'A': [{
                        'friend_id':
                        'friend_name':
                        'gender':
                        'mcode':
                        'qrcode':
                        'phone_no':
                        'email':
                        'portrait_url':
                        'city_id':
                        'city_name':
                        'name':
                        'birthday':
         }]}}
         
## /userweb/(\w+)/favorites?offset=0&limit=1
    get: //查询用户收藏
    response: 
    {
        'total_num': total_num,
        'goods': [{'id': id
                   "desp": desp
                   "price": price
                   "promot": promot
                   "picList": picList
                   "basic": basic
                   "status": status
                   }]
    }
    
    
## /userweb/shopgoods/1, 2, 3
    get: //查询商店中的商品信息, 可以一次传入多个商店
    response:
    {
        'total_num': len(shop_ids), 
        'shops': [{'shop_id': shop_id, 'shop_name': shop_name, 'goods': goods_list}
    }
    
## /userweb/search/手机号或喵喵号
    get: //通过手机号或喵喵号搜索用户
    response: {
        "user_id"
        "name"
        "gender"
        "birthday"
        "mcode"
        "qrcode"
        "phone_no"
        "email"
        "portrait_url"
        "city_id"
        "city_name"
    }
    
## /userweb/(.*)/friend/remark
    post: //修改用户备注名
        {
            "friend_id": //用户id 
            "remark": //用户备注名
        }
        response: {
            "is_success": True
        }

## /userweb/qqinfo/(\w+)
    get: //取得qq登陆的用户信息
    params: assess_token
    response: userinfo 返回腾讯返回的信息

## /userweb/weiboinfo/(\w+)
    get: //取得微博用户登录的用户信息
    params: code
    response: userinfo 返回新浪返回的用户信息


## /user/goods/promot/news?gid=1&gid=2
    get: //取得多件商品信息
        response:  
        {
            'goods': [{'id'
                       "desp"
                       "price":
                       "promot":
                       "picList":
                       "basic":
                       "status": //satus = 1: 上架商品; =0 or 2, 下架商品
                       }]
        }

## /userweb/thirdlogin/wechat/info?access_token=&open_id=
    get: //取得微信信息
    params: {
        "access_token":
        "open_id"
    }
    response: userinfo 返回微信返回的用户信息

## /userweb/imgupload?url=
    get: //通过url上传图片至图片服务器
    params: url,
    response: {
        is_success: True, 
        url: "http://1.png
    }
    
## /userweb/quickmodifyimg
    get: //通过url快速修改用户头像
        params: 
            {
                "user_id": 11,
                 "url": "http://111.png"
            }
        response: 
            {'is_success': True}
            
## /userweb/selectphones
    post: 批量查询号码是否是 非平台用户/平台用户好友/平台用户非好友
    {
        phone: 本机号码
        phone_list: 号码列表
    }
    response: {
        'platform_friend': [1875689898, xx, xx], 
        'platform_notfriend': [], 
        'notplatform': []
    }
    

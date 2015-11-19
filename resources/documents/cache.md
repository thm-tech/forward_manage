## 缓存数据
* 公司信息接口(1天): /basic/companyinfo
* 省市接口(1天): /basic/city/(.*)
* 类别接口(1天): /basic/goodscategories

* 首页活动接口(1小时): /user/activity
* 首页商店列表展示接口(1小时): /user/shop

* 品牌推荐端口(1天): user/shop/recommend

* 用户端商店商品接口(不影响商家端, 1小时): userweb/shopgoods
* 用户端商店商品接口2(不影响商家端, 1小时): user/goods

* 用户端商店信息接口(1天): /user/shop/info

## 说明
* 请求的哈希值计算: md5(url + body)
* 缓存失效条件: redis 中数据可设置失效时间, 失效后该数据即不可被读取.

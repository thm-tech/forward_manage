## 生产环境

host: 112.124.115.140

user/password: web/forward2015

    ; forward 后台
    cd /home/web/forward/forward
    python main.py
    
    ; forward 管理后台
    cd /home/web/forward_manage
    python main.py
    
    ; forward 后台更新
    cd /home/ywb/forward
    git pull origin master
    python3.5 release.py --mt
    
    ; forward 管理后台更新
    cd /home/web/release
    python3.5 release_manage.py
    
## 开发环境

host: 115.28.143.67

user/password: ywb/ywb

    ; forward 后台
    cd /home/ywb/forward/forward
    python main.py
    
    ; forward 管理后台
    cd /home/ywb/forward_manage
    python main.py
    
    ; forward 后台更新
    cd /home/ywb/forward
    git pull origin master
    
    ; forward 管理后台更新
    cd /home/ywb/forward_manage
    git pull origin master
    
    
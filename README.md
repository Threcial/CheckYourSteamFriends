# CheckYourSteamFriends

使用此脚本无需登录，但需要公开好友列表

尚在开发...

## 使用方法

1. 修改`snapshot.py`脚本内`URL`和`PROXIES`

    `URL`可以通过点击`Steam`个人名称中的好友后左上角链接获得

    `PROXIES`即你的代理端口

###
URL示例：https://steamcommunity.com/profiles/*************/friends/

PROXIES示例：http://127.0.0.1:7890
###

2. 运行`snapshot.py`，将会在当前目录下创建`JSON`文件夹，存放`json`文件记录当前所有好友信息，包括steamid，steam名字，个人资料地址，头像图片地址，可用记事本查看，命名规则为记录时间和当前好友数量。

3. 如果之前有记录过那么会自动对比上一次记录，提供好友的变动信息。

4. 脚本用于比对任意两个记录间的变动

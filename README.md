# CheckYourSteamFriends

一个临时脚本：抓取指定 Steam 个人资料页的好友列表（无需登录但**需要公开好友列表**），提取：
- steamid
- name
- href（个人资料链接）
- img（头像链接）

并将结果保存为 JSON（按时间戳与当前好友数量命名），同时读取本地历史最新 JSON，与本次数据对比输出：
- 新增好友数量与列表
- 失去好友数量与列表

> 注意：本脚本依赖页面 HTML 结构（XPath）和网络环境；Steam 的Frinds网页页面结构变化可能导致解析失败。

---

## 目录结构

运行后会在脚本同级目录创建 `JSON/` 文件夹：
```
CheckYourSteamFriends/
├── snapshot.py
└── JSON/
    ├── 20251228161523-33.json
    ├── 20251229103010-35.json
    └── 20251230110452-36.json
```

文件命名规则：
- `YYYYMMDDHHMMSS-好友数量.json`
- 例如：`20251228161523-33.json`

---

## 环境要求

- Python 3.9+（推荐 3.10/3.11）
- 依赖：
  - requests
  - lxml

安装依赖：

```bash
pip install -r requirements.txt
```

---

## 使用方法

打开脚本，确认目标 URL：
```python
URL = "https://steamcommunity.com/profiles/xxxxxxxxxxxxxxxxx/friends/"
```

如需代理，修改PROXIES：
```python
PROXIES = "http://127.0.0.1:7890"
os.environ["HTTP_PROXY"] = PROXIES
os.environ["HTTPS_PROXY"] = PROXIES
```

如果你不需要代理，请注释/删除上述三行（PROXIES + 两个环境变量）。

运行脚本：
```
python snapshot.py
```

运行结束后：

- 会将本次抓取结果写入 JSON/ 目录

- 会读取 JSON/ 目录下“命名规则匹配且最新”的一个历史文件用于对比

- 命令行输出新增/失去好友信息

- 最后等待回车退出

---

## 免责声明

仅供学习与个人用途。请遵守 Steam 的服务条款与相关法律法规。


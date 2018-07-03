###一、使用方法

0. 该项目仅适合于简单的项目
1. 确保开发机上有python，且版本在3.5以上
2. 项目跟目录下执行 ```python3 -m venv venv && source ./venv/bin/active```
3. 执行 ```pip install -r requirements.txt``` 安装项目所需要的包
4. 执行 ``` python3 run.py ```即启动了项目


### 二、目录结构说明
 ```bash

.
├── README.md
├── logs
├── main
│   ├── __init__.py
│   ├── api # 项目的逻辑代码
│   ├── common # 公共的库，比如logger，建立mysql连接等。
│   └── resource # 存放静态文件的目录
├── requirements.txt # 依赖包配置项
└── run.py # 启动入库

```

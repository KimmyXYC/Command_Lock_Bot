# Command Lock Bot
## 功能 / Features
```
lock_cmd - 锁定命令
unlock_cmd - 解锁命令
list_locked_cmd - 查看已锁定命令
```
## 安装 / Installation

- 安装依赖。Install dependencies.
```shell
git clone https://github.com/KimmyXYC/Command_Lock_Bot.git
pip3 install -r requirements.txt
```

- 复制配置文件。Copy configuration file.
```shell
cp Config/app_exp.toml Config/app.toml
```
- 填写配置文件。Fill out the configuration file.
```toml
[bot]
master = [100, 200]
botToken = 'key' # Required, Bot Token


[proxy]
status = false
url = "socks5://127.0.0.1:7890"
```
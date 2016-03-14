# chunyun

一个通用的数据库迁移工具, 目前仅支持postgres

![Alt text](screenrecorder.gif)


[![Build Status](https://travis-ci.org/erhuabushuo/chunyun.svg?branch=master)](https://travis-ci.org/erhuabushuo/chunyun)


## 安装

    pip install chunyun

## 操作

在当前目录建立

    chunyun create .

配置config.ini并初始化

    chunyun init

同步

    chunyun sync

回滚

    chunyun rollback 
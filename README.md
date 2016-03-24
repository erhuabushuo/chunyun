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

## 什么是数据库迁移

数据库模式的 CI 称为 CDBI（Continuous DataBase Integration），
但是比起CDBI，使用从RoR的工具名(Migration)衍生而来的“数据迁移”整个叫法似乎更多一些

## 数据迁移的功能

* 管理 SQL 执行的顺序和需要执行哪些 SQL
* 管理模式定义编辑的冲突
* 提供回滚的机制
* 支持数据的加载

## 常用的数据库迁移工具

* Migration（Ruby on Rails）
* south（Django）
* Yii Migrations

Flyway, Liquibase, dbdeploy

## 为什么要数据库迁移

* 集中管理
* 防止遗漏
* 快速回滚
* 快速部署
* CI重要环节

## 我为什么要重复造轮子

* 通用
* Raw SQL
* 兼容已有系统

## TODO

* multiple engines supporting



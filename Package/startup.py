#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from SystemMgr import SystemMgr


def usage():
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--svn", type=str, required=False, default='*', help="svn要更新到的版本号, 请输入数字或者*")
    parser.add_argument("--compile", required=False, action="store_true", help="是否编译源码, 有此选项则编译源码")
    parser.add_argument("--env", type=str, required=True, choices=["lt", "pt", "pd"], default="lt",
                        help="对应打包环境,lt,pt,pd")
    parser.add_argument("--package", required=False, action="store_true", help="是否打包, 有此选项则将当前环境进行打包并发布")
    args = parser.parse_args()
    return args


def main():
    args = usage()
    system_mgr = SystemMgr()
    system_mgr.run(args) # send args into this function


if __name__ == '__main__':
    main()

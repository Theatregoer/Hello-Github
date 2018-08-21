#!/usr/bin/python
# -*- coding: utf-8 -*-
from compile.CompileMgr import Compile
from svn.SvnMgr import SvnMgr
from pack_and_pulish.PackMgr import PackAndPublish


class SystemMgr:
    def __init__(self):
        self.svn_mgr = SvnMgr()
        self.com = Compile()
        self.pack = PackAndPublish()
        pass

    def run(self, args):
        # 将源代码恢复到指定版本
        if args.svn:
            # print('开始更新到指定版本')
            self.svn_mgr.run(args.svn)
            # print('已更新至指定版本')

        # 针对源代码进行编译, 根据编译环境决定编译哪个版本
        if args.compile:
            # print('开始编译')
            self.com.compile(args.env)
            # print('编译完毕')

        # 对源代码打包PackMgr()
        if args.package:
            # print('开始打包并发布源文件')
            self.pack.run(args.env, args.svn)
            # print('打包发布完毕')



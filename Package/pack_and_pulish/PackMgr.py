#!/usr/bin/python
# -*- coding: utf-8 -*-
from zip.ZipManage import ZipManage
import os
import file_dictionary
from FileMgr.FileMgr import CopyMove
import Conf
import time
from svn.SvnMgr import SvnMgr
import shutil


class PackAndPublish(object):
    def __init__(self):
        self.zip = ZipManage()
        self.copy = CopyMove()
        self.svn = SvnMgr()
        self.localtime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取时间
        pass

    def CopyDictionary(self, compiled_exe_dir, exe_copy_product_dir):
        # 循环打印key,并导入操作地址
        for key in file_dictionary.file_dictionary.keys():
            source_key_dir = os.path.join(compiled_exe_dir, key)  # 打包源文件夹下和dictionary中key合成的文件路径
            target_key_dir = os.path.join(exe_copy_product_dir, key)  # 拷贝目标文件夹下和dictionary中key合成的文件路径
            # print(os.path.abspath(os.path.join(target_key_dir,"..")))
            # 判断目标地址是否存在后进行复制操作
            if os.path.isfile(source_key_dir):
                up_exe_copy_product_dir = os.path.abspath(os.path.join(target_key_dir, ".."))
                if not os.path.exists(up_exe_copy_product_dir):  # 如果目标地址不存在则创建目标地址后再拷贝
                    os.makedirs(up_exe_copy_product_dir)
                    self.copy.copyFolder(source_key_dir, target_key_dir)
                if os.path.exists(up_exe_copy_product_dir):  # 目标地址存在直接拷贝文件
                    self.copy.copyFolder(source_key_dir, target_key_dir)

    def ZipExe(self, compiled_exe_dir, zip_exe_target_dir, file_type, version_number):
        # 生成指定文件名
        filename = r'%s\%s-%s-%s.exe' % (zip_exe_target_dir, self.localtime, file_type, version_number)
        self.zip.make_zip(compiled_exe_dir, zip_exe_target_dir, filename)

    def PackPdb(self, compiled_exe_dir, pdb_target_dir):
        for file in os.listdir(compiled_exe_dir):
            source_file = os.path.join(compiled_exe_dir, file)  # 源文件夹下的文件路径
            target_file = os.path.join(pdb_target_dir, file)  # 生成pdb文件夹下的文件路径
            if os.path.splitext(source_file)[1] == Conf.PDB_TAIL:  # 判断是否pdb文件
                up_target_file = os.path.abspath(os.path.join(target_file, ".."))
                if not os.path.exists(up_target_file):  # 判断目标路径是否存在
                    os.makedirs(up_target_file)
                    shutil.copy(source_file, target_file)  # 对文件进行复制
                if os.path.exists(up_target_file):
                    shutil.copy(source_file, target_file)
            if os.path.isdir(source_file):  # 如果文件夹下依然是文件夹，调用自身
                self.PackPdb(source_file, target_file)

    def ZipPdb(self, pdb_source_dir, pdb_pack_target_dir, file_type, version_number):
        # 生成指定文件名
        filename = r'%s\%s-%s-kvclient-%s-pdb.rar' % (pdb_pack_target_dir, self.localtime, file_type, version_number)
        self.zip.make_zip(pdb_source_dir, pdb_pack_target_dir, filename)

    def CopyPdb(self, pdb_source_dir, pdb_copy_target_dir):
        self.copy.copyFolder(pdb_source_dir, pdb_copy_target_dir)

    def MakePublishFolder(self, public_dir):
        publish_dir = os.path.join(public_dir, self.localtime)  # 在总发布文件夹下的本次发布文件夹路径
        publish_pdb_dir = os.path.join(public_dir, self.localtime, Conf.PDB_FILE)  # 在本次发布文件夹下的用于存放pdb文件的文件夹的路径
        if not os.path.exists(publish_dir):  # 判断打包文件夹是否存在
            os.makedirs(publish_dir)   # 创建文件夹
        if not os.path.exists(publish_pdb_dir):  # 判断打包文件夹是否存在
                os.makedirs(publish_pdb_dir)  # 创建打包文件夹

    def PublishExe(self, pack_exe_source_dir, public_dir, file_type, version_number):
        publish_exe_target_dir = os.path.join(public_dir, self.localtime)  # EXE文件发布路径
        # 在Pack文件夹下被打包好的EXE文件地址
        new_pack_exe_source_dir = r'%s\%s-%s-%s.exe' % (pack_exe_source_dir, self.localtime, file_type, version_number)
        shutil.move(new_pack_exe_source_dir, publish_exe_target_dir)

    def PublishPdb(self, pdb_pack_dir, public_dir, file_type, version_number):
        puslish_pdb_target_dir = os.path.join(public_dir, self.localtime, Conf.PDB_FILE)  # pdb文件发布路径
        # 在Pack文件夹下被打包好的pdb文件地址
        shutil.move(r'%s\%s-%s-kvclient-%s-pdb.rar' %
                             (pdb_pack_dir, self.localtime, file_type, version_number), puslish_pdb_target_dir)

    def run(self, file_type, version_number):
        if version_number == "*":
            version_number = self.svn.get_version(Conf.SOURCE_CODE_DIR)  # 如果update到svn最新版本,调用svn函数获取最新版本号
        if file_type == "lt":
            compiled_file = Conf.COMPILE_BINARY_DIR_LT  # 被编译后文件的地址
        elif file_type == "pt":
            compiled_file = Conf.COMPILE_BINARY_DIR_PT
        elif file_type == "pd":
            compiled_file = Conf.COMPILE_BINARY_DIR_PD
        self.CopyDictionary(compiled_file, Conf.PRODUCT_DIR)  # 将编译好的二进制文件与pdb文件拷贝至指定目录
        pack_dir = os.path.join(os.getcwd(), Conf.PACK_TARGET_DIR)  # 生成打包文件夹的路径
        if not os.path.exists(pack_dir):  # 判断打包文件夹是否存在
            os.makedirs(pack_dir)   # 创建打包文件夹
        self.ZipExe(compiled_file, pack_dir, file_type, version_number)  # 针对二进制文件,打包成exe,并改名
        save_pdb_dir = os.path.join(pack_dir, Conf.PDB_FILE)  # 在打包文件夹下再创建一个用于存放pdb文件的文件夹
        if os.path.exists(save_pdb_dir):
            print('pdb文件夹已存在,本次操作将覆盖原文件夹')
        if not os.path.exists(save_pdb_dir):
            os.makedirs(save_pdb_dir)  # 创建存放pdb文件的文件夹
        self.PackPdb(compiled_file, save_pdb_dir)  # 将编译后文件夹中的pdb文件移动至创建的存放pdb文件夹中
        copy_pdb_dir = os.path.join(os.getcwd(), Conf.COPY_TARGET_DIR)  # 生成拷贝文件夹的路径
        if not os.path.exists(copy_pdb_dir):  # 判断pdb拷贝文件夹是否存在
            os.makedirs(copy_pdb_dir)  # 创建复制文件夹
        self.CopyPdb(save_pdb_dir, copy_pdb_dir)  # 备份PDB文件
        self.ZipPdb(save_pdb_dir, pack_dir, file_type, version_number)  # 针对pdb压缩成zip并改名
        self.MakePublishFolder(Conf.PUBLIC_DIR)  # 创建发布文件夹
        self.PublishExe(pack_dir, Conf.PUBLIC_DIR, file_type, version_number)  # 拷贝EXE包
        self.PublishPdb(pack_dir, Conf.PUBLIC_DIR, file_type, version_number)  # 拷贝pdb包


import shutil
import os
import re
import Conf


class SvnMgr(object):
    def __init__(self):
        pass

    def svn_commit(self, target_dir):
        add_command = 'svn add %s' % target_dir
        os.system(add_command)  # 纳入版权控制
        note = input('备注：')
        commit_command = 'svn commit -m %s %s' % (note, target_dir)
        os.system(commit_command)  # cmd语句实现

    def svn_update(self, version_number, target_dir):
        if version_number == '*':
            update_command = 'svn update %s' % target_dir
        else:
            update_command = 'svn update -r %s %s' % (version_number, target_dir)
        os.system(update_command)

    def svn_delete(self, target_dir):
        if os.path.isdir(target_dir):  # 判断目标地址是否为目录
            shutil.rmtree(target_dir)  # 删除目录
        else:
            os.remove(target_dir)

    def svn_revert(self, target_dir):
        revert_command = 'svn revert -R %s' % target_dir
        os.system(revert_command)

    def svn_cleanup(self, target_dir):
        cleanup_command = 'svn cleanup %s' % target_dir
        os.system(cleanup_command)

    def get_version(self, target_dir):
        var = os.popen('svn info %s' % target_dir).read()
        var_list = var.splitlines()  # 保留换行符
        for str in var_list:
            if str.find('Revision:') >= 0:
                version = re.findall("\d+", str)  # 正则表达式处理换行符
                return version[0]

    def run(self, version_number):
        self.svn_cleanup(Conf.SOURCE_CODE_DIR)  # 清理文件残余
        self.svn_revert(Conf.SOURCE_CODE_DIR)  # 将文件回滚至初始版本
        self.svn_update(version_number, Conf.SOURCE_CODE_DIR)  # 更新文件至指定版本


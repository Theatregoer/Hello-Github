import shutil
import os
import re


class SvnMgr(object):
    def __init__(self, targetDir):
        self.targetDir = targetDir

    def svncommit(self):
        os.system('svn add %s' % self.targetDir)#纳入版权控制
        note = input('备注：')
        os.system('svn commit -m %s %s' % (note, self.targetDir))#cmd语句实现

    def svnupdate(self):
        revision = input('请输入版本号：')
        os.system('svn update -r %s %s' % (revision, self.targetDir))

    def svndelete(self):
        if os.path.isdir(self.targetDir):#判断目标地址是否为目录
            shutil.rmtree(self.targetDir)
        else:
            os.remove(self.targetDir)

    def svnrevert(self):
        targetre = input('请输入目标版本号：')
        os.system('svn merge -r %s:%s %s' % (SvnMgr.getversion(self.targetDir), targetre, self.targetDir))

    def svncleanup(self):
        os.system('svn cleanup %s' % self.targetDir)

    def getversion(self):
        var = os.popen('svn info %s' % self.targetDir).read()
        list = var.splitlines()#保留换行符
        for str in list:
            if str.find('Revision:') >= 0:
                version = re.findall("\d+", str)#正则表达式处理换行符
                print(version[0])
        return version[0]


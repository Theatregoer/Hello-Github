import os
import shutil


class CopyMove(object):

    def __init__(self):
        pass

    def copyFolder(self, sourceDir, targetDir):
        if os.path.isfile(sourceDir):
                shutil.copy(sourceDir, targetDir)
        if os.path.isdir(sourceDir):
            if targetDir.split("\\")[-1] != sourceDir.split("\\")[-1]:
                targetDir = r'%s\%s' % (targetDir, sourceDir.split("\\")[-1])
            for f in os.listdir(sourceDir):  # 通过原文件夹创建文件目录
                sourceF = os.path.join(sourceDir, f)
                targetF = os.path.join(targetDir, f)
                if os.path.isfile(sourceF):  # 如果原文件夹中的文件存在
                    if not os.path.exists(targetDir):  # 目标文件夹不存在
                        os.makedirs(targetDir)  # 创建一个目标文件夹
                    if not os.path.exists(targetF) or (os.path.exists(targetF)
                        and (os.path.getsize(targetF) != os.path.getsize(sourceF))):  # 如果目标文件不存在或大小不同则覆盖
                        shutil.copy(sourceF, targetF)  # 对文件进行复制
                if os.path.isdir(sourceF):
                    self.copyFolder(sourceF, targetF)  # 对原文件夹内的文件夹进行复制
import zipfile
import os


class ZipManage(object):
    def __init__(self, sourceDir, targetDir):
        self.sourceDir = sourceDir
        self.targetDir = targetDir

    def make_zip(self):
        output_filename = r'%s\%s.zip' % (self.targetDir, self.sourceDir.split("\\")[-1])  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
        zipf = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_STORED)
        pre_len = len(os.path.dirname(self.sourceDir))
        for parent, dirnames, filenames in os.walk(self.sourceDir):
            for filename in filenames:self.sourceDir.split("\\")[-1]
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep) #相对路径
            zipf.write(pathfile, arcname)
            zipf.close()

    def unzip_file(self):
        r = zipfile.is_zipfile(self.sourceDir)
        if r:
            fz = zipfile.ZipFile(self.sourceDir, 'r')
            for file in fz.namelist():
                fz.extract(file, self.targetDir)
        else:
            print('This is not zip')








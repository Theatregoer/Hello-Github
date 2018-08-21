import zipfile
import os


class ZipManage(object):
    def __init__(self):
        pass

    def make_zip(self, sourceDir, targetDir, filename):
        output_filename =os.path.join(targetDir, filename)  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
        zipf = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_STORED)
        pre_len = len(os.path.dirname(sourceDir))
        for parent, dirnames, filenames in os.walk(sourceDir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

    def unzip_file(self, sourceDir, targetDir):
        r = zipfile.is_zipfile(sourceDir)
        if r:
            fz = zipfile.ZipFile(sourceDir, 'r')
            for file in fz.namelist():
                fz.extract(file, targetDir)
        else:
            print('This is not zip')






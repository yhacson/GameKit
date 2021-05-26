import os

fileDir = os.path.abspath(os.path.dirname(__file__))
projDir = os.path.abspath(os.path.join(fileDir, ".."))
interfaceDir = os.path.join(projDir, "binding", "interface")

# make dir if not exist. if already exist, do nothing
def mkdirs(dir):
    folder = os.path.exists(dir)
    if not folder:
        os.makedirs(dir)

def getSrcDir():
    srcDir = os.path.join(projDir, "src")
    return srcDir

# @paths .i文件路径
def getWrapFilePath(*paths):
    # 把 dir/file.i 转换为 dir_file_wrap.cxx 文件名格式
    fileName = ""
    for i in range(0, len(paths)):
        p = paths[i]
        if(i == len(paths)-1):
            p = p.strip(".i")
            p = p + "_wrap.cxx"
        fileName = os.path.join(fileName, p)
    fileName = fileName.replace(os.path.sep, "_")
    filePath = os.path.join(projDir, "binding", "auto_gen", "wrap", fileName)
    return filePath
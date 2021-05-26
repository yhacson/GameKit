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
    filePath = os.path.join(projDir, "binding", "auto_gen", "wrap")
    # 把 file.i 转换为 file_wrap.cxx 文件名格式
    for i in range(0, len(paths)):
        p = paths[i]
        if(i == len(paths)-1):
            p = p.strip(".i")
            p = p + "_wrap.cxx"
        filePath = os.path.join(filePath, p)
    return filePath
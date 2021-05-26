import os

fileDir = os.path.abspath(os.path.dirname(__file__))
projDir = os.path.abspath(os.path.join(fileDir, ".."))
interfaceDir = os.path.join(projDir, "binding", "interface")

# make dir if not exist. if already exist, do nothing
def mkdirs(dir):
    folder = os.path.exists(dir)
    if not folder:
        os.makedirs(dir)

# get auto wrap cpp files dir
def getWrapCppDir():
    cppDir = os.path.join(projDir, "binding", "auto_gen", "wrap")
    mkdirs(cppDir)
    return cppDir

def getSrcDir():
    srcDir = os.path.join(projDir, "src")
    return srcDir

# get auto gen c# files dir
def getGenCSDir():
    csDir = os.path.join(projDir, "binding", "auto_gen", "csharp")
    mkdirs(csDir)
    return csDir
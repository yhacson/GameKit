import os
import common

# 命令行参数
# @paths .i文件的路径，可变输入参数
def getCmdParams(ns, *paths):
    pd = {}
    pd["srcDir"] = common.getSrcDir() # cpp源码
    pd["outDir"] = os.path.join(common.projDir, "binding", "auto_gen", "csharp") # 自动生成的C#代码
    pd["iFile"] = os.path.join(common.interfaceDir, *paths) # swig .i接口文件
    pd["wrapFile"] = common.getWrapFilePath(*paths) # 重新封装的wrap文件
    pd["namespace"] = ns
    return pd

# 生成wrap文件
def genWrapFiles():
    wrapParamList = []
    wrapParamList.append(getCmdParams("GameKit.System", "system", "Platform.i")) # system/Platform

    for p in wrapParamList:
        common.mkdirs(p["outDir"])
        common.mkdirs(os.path.dirname(p["wrapFile"]))
        cmd = "swig -c++ -csharp -namespace %(namespace)s -outdir %(outDir)s -o %(wrapFile)s -I%(srcDir)s %(iFile)s" % p
        os.system(cmd)

def main():
    genWrapFiles()

if __name__ == "__main__":\
    main()
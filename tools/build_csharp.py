import os
import common

def getParamsDict():
    pd = {
        "outDir" : common.getGenCSDir(),
        "srcDir" : common.getSrcDir()
    }
    return pd

def main():
    params = getParamsDict()
    params["wrapFile"] = os.path.join(common.getWrapCppDir(), "GameKit_wrap.cxx")
    params["iFile"] = os.path.join(common.interfaceDir, "GameKit.i")
    cmd = "swig -c++ -csharp -outdir %(outDir)s -o %(wrapFile)s -I%(srcDir)s %(iFile)s" % params
    os.system(cmd)

if __name__ == "__main__":\
    main()
include(${CMAKE_CURRENT_LIST_DIR}/Var.cmake)

set(SrcDir ${ProjWorkspace}/src)

set(HeaderCpp
    ${SrcDir}/GameKit.h
    ${SrcDir}/System/Platform.h
    ${SrcDir}/Runtime.h
)

set(SrcCpp
    ${SrcDir}/Runtime.cpp
)
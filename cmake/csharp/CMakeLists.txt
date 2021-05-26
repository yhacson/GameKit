cmake_minimum_required(VERSION 3.0.0)

# 工程名称
project(GameKit)

include(../modules/SrcList.cmake)
include(../modules/WrapList.cmake)

# 设置
set(CMAKE_CXX_STANDARD 11)
set(GameKitHeader
    ${HeaderCpp})
set(GameKitSrc
    ${SrcCpp}
    ${SrcWrap})

list(APPEND GameKitLib ${GameKitHeader} ${GameKitSrc})

# 编译源码生成目标
add_library(GameKit SHARED ${GameKitLib})
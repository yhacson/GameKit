#pragma once

#include "GameKit.h"

NS_GK_BEG

class Runtime
{
public:
    static unsigned int CurPlatformType();
    static const char *CurPlatformStr();
};

NS_GK_END
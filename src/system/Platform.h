#pragma once

#include "../GameKit.h"

NS_GK_SY_BEG

class Platform
{
public:
    static unsigned int GetType();
    static const char *GetString();

public:
    static const unsigned int Unknow;
    static const unsigned int Windows;
    static const unsigned int Android;
    static const unsigned int IOS;
};

NS_GK_SY_END
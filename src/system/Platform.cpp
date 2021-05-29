#include "Platform.h"

NS_GK_SY_BEG

const unsigned int Platform::Unknow = 0;
const unsigned int Platform::Windows = 1;
const unsigned int Platform::Android = 2;
const unsigned int Platform::IOS = 3;

unsigned int Platform::GetType()
{
    auto type = Platform::Unknow;
#ifdef _WIN32
    type = Platform::Windows;
#elif __ANDROID__
    type = Platform::Android;
#elif __APPLE__
    type = Platform::IOS;
#endif
    return type;
}

const char *Platform::GetString()
{
    auto type = GetType();
    char *str = "Unknow";
    switch (type)
    {
    case Windows:
        str = "Windows";
        break;

    case Android:
        str = "Android";
        break;

    case IOS:
        str = "iOS";
        break;

    case Unknow:
    default:
        str = "Unknow";
        break;
    }

    return str;
}

NS_GK_SY_END
#include "Runtime.h"
#include "system/Platform.h"

NS_USING_GK
NS_USING_GK_SY

unsigned int Runtime::CurPlatformType()
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

const char *Runtime::CurPlatformStr()
{
    auto type = CurPlatformType();
    char *str = "Unknow";
    switch (type)
    {
    case Platform::Windows:
        str = "Windows";
        break;

    case Platform::Android:
        str = "Android";
        break;

    case Platform::IOS:
        str = "iOS";
        break;

    case Platform::Unknow:
    default:
        str = "Unknow";
        break;
    }

    return str;
}
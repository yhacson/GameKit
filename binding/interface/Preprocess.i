#ifndef _UTILS_I_
#define _UTILS_I_

%define INCLUDE_SRC(FILE)
%{
#include "../../../src/FILE"
%}
%enddef

%define USING_NS(NS)
%{
using namespace NS;
%}
%enddef

#endif
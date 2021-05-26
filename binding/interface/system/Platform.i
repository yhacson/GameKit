%include "../Preprocess.i"

INCLUDE_SRC(system/Platform.h)
%{
using namespace Luxkit::System;
%}

// GET_SRC_PATH(system/Platform.h)
%include "system/Platform.h"
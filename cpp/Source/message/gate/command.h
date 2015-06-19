/*
* @filename command.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_GATE_COMMAND_H__
#define __MESSAGE_GATE_COMMAND_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>

namespace message{
    namespace gate{
        namespace command{

            // enum class ETestCommand
            enum class ETestCommand
            {
                FirstMessage = 10001,
            };
            void read(gamit::CSerializer & __is, ETestCommand & __val);
            void write(gamit::CSerializer & __os, ETestCommand __val);

        }
    }
}

#endif //__MESSAGE_GATE_COMMAND_H__

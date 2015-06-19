/*
* @filename command.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/gate/command.h>

void message::gate::command::read(gamit::CSerializer & __is, message::gate::command::ETestCommand &__val)
{
    int __i = 0;
    __is.read(__i);
    __val = message::gate::command::ETestCommand(__i);
}

void message::gate::command::write(gamit::CSerializer & __os, message::gate::command::ETestCommand __val)
{
    __os.write(int(__val));
}


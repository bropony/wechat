/*
* @filename etest.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/common/etest.h>

void message::common::etest::read(gamit::CSerializer & __is, message::common::etest::EHelloWorld &__val)
{
    int __i = 0;
    __is.read(__i);
    __val = message::common::etest::EHelloWorld(__i);
}

void message::common::etest::write(gamit::CSerializer & __os, message::common::etest::EHelloWorld __val)
{
    __os.write(int(__val));
}

// implementation of class SHelloEnum
std::string message::common::etest::SHelloEnum::_msgName("SHelloEnum");

void message::common::etest::SHelloEnum::regist()
{
    gamit::MessageBlock::registCreateFunc("SHelloEnum", SHelloEnum::create);
}

const message::common::etest::SHelloEnumPtr message::common::etest::SHelloEnum::create()
{
    return (new SHelloEnum());
}

void message::common::etest::SHelloEnum::__read(gamit::CSerializer & __is)
{
    __is.read(age);
    __is.read(damn);
    message::common::etest::read(__is, greetType);
}

void message::common::etest::SHelloEnum::__write(gamit::CSerializer & __os) const
{
    __os.write(age);
    __os.write(damn);
    message::common::etest::write(__os, greetType);
}

const std::string & message::common::etest::SHelloEnum::__name() const
{
    return _msgName;
}


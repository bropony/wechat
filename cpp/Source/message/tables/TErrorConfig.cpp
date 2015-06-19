/*
* @filename TErrorConfig.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/tables/TErrorConfig.h>

// implementation of class TErrorConfig
gamit::CAutoRun registTErrorConfig(message::tables::TErrorConfig::TErrorConfig::regist);
std::string message::tables::TErrorConfig::TErrorConfig::_msgName("TErrorConfig");

void message::tables::TErrorConfig::TErrorConfig::regist()
{
    gamit::MessageBlock::registCreateFunc("TErrorConfig", TErrorConfig::create);
}

const message::tables::TErrorConfig::TErrorConfigPtr message::tables::TErrorConfig::TErrorConfig::create()
{
    return (new TErrorConfig());
}

void message::tables::TErrorConfig::TErrorConfig::__read(gamit::CSerializer & __is)
{
    __is.read(errorCode);
    __is.read(errorName);
    __is.read(errorStr);
}

void message::tables::TErrorConfig::TErrorConfig::__write(gamit::CSerializer & __os) const
{
    __os.write(errorCode);
    __os.write(errorName);
    __os.write(errorStr);
}

const std::string & message::tables::TErrorConfig::TErrorConfig::__name() const
{
    return _msgName;
}

void message::tables::TErrorConfig::__read(gamit::CSerializer & __is, message::tables::TErrorConfig::SeqTErrorConfig & __valList, __SeqTErrorConfig_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        message::tables::TErrorConfig::TErrorConfig __val;
        __val.__read(__is);
        __valList.push_back(__val);
    }
}

void message::tables::TErrorConfig::__write(gamit::CSerializer & __os, const message::tables::TErrorConfig::SeqTErrorConfig & __valList, __SeqTErrorConfig_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __val.__write(__os);
    }
}


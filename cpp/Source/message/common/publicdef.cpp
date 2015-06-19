/*
* @filename publicdef.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/common/publicdef.h>

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::SeqInt & __valList, __SeqInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        int __val;
        __is.read(__val);
        __valList.push_back(__val);
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::SeqInt & __valList, __SeqInt_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __os.write(__val);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::SeqLong & __valList, __SeqLong_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        long64_t __val;
        __is.read(__val);
        __valList.push_back(__val);
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::SeqLong & __valList, __SeqLong_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __os.write(__val);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::SeqString & __valList, __SeqString_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        std::string __val;
        __is.read(__val);
        __valList.push_back(__val);
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::SeqString & __valList, __SeqString_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __os.write(__val);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::SeqFloat & __valList, __SeqFloat_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        float __val;
        __is.read(__val);
        __valList.push_back(__val);
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::SeqFloat & __valList, __SeqFloat_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __os.write(__val);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::DictIntInt & __valDict, __DictIntInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        int __key;
        int __val;
        __is.read(__key);
        __is.read(__val);
        __valDict.insert({__key, __val});
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::DictIntInt & __valDict, __DictIntInt_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __os.write(__pair.second);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::DictIntString & __valDict, __DictIntString_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        int __key;
        std::string __val;
        __is.read(__key);
        __is.read(__val);
        __valDict.insert({__key, __val});
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::DictIntString & __valDict, __DictIntString_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __os.write(__pair.second);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::DictStringInt & __valDict, __DictStringInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        std::string __key;
        int __val;
        __is.read(__key);
        __is.read(__val);
        __valDict.insert({__key, __val});
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::DictStringInt & __valDict, __DictStringInt_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __os.write(__pair.second);
    }
}

void message::common::publicdef::__read(gamit::CSerializer & __is, message::common::publicdef::DictStringString & __valDict, __DictStringString_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        std::string __key;
        std::string __val;
        __is.read(__key);
        __is.read(__val);
        __valDict.insert({__key, __val});
    }
}

void message::common::publicdef::__write(gamit::CSerializer & __os, const message::common::publicdef::DictStringString & __valDict, __DictStringString_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __os.write(__pair.second);
    }
}


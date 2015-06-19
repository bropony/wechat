/*
* @filename gatemsg.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/gate/gatemsg.h>

void message::gate::gatemsg::__read(gamit::CSerializer & __is, message::gate::gatemsg::SeqSeqInt & __valList, __SeqSeqInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        message::common::publicdef::SeqInt __val;
        message::common::publicdef::__read(__is, __val, message::common::publicdef::__SeqInt_U__());
        __valList.push_back(__val);
    }
}

void message::gate::gatemsg::__write(gamit::CSerializer & __os, const message::gate::gatemsg::SeqSeqInt & __valList, __SeqSeqInt_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        message::common::publicdef::__write(__os, __val, message::common::publicdef::__SeqInt_U__());
    }
}

void message::gate::gatemsg::__read(gamit::CSerializer & __is, message::gate::gatemsg::SeqDictIntInt & __valList, __SeqDictIntInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        message::common::publicdef::DictIntInt __val;
        message::common::publicdef::__read(__is, __val, message::common::publicdef::__DictIntInt_U__());
        __valList.push_back(__val);
    }
}

void message::gate::gatemsg::__write(gamit::CSerializer & __os, const message::gate::gatemsg::SeqDictIntInt & __valList, __SeqDictIntInt_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        message::common::publicdef::__write(__os, __val, message::common::publicdef::__DictIntInt_U__());
    }
}

void message::gate::gatemsg::__read(gamit::CSerializer & __is, message::gate::gatemsg::DictDictStringInt & __valDict, __DictDictStringInt_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        int __key;
        message::common::publicdef::DictStringInt __val;
        __is.read(__key);
        message::common::publicdef::__read(__is, __val, message::common::publicdef::__DictStringInt_U__());
        __valDict.insert({__key, __val});
    }
}

void message::gate::gatemsg::__write(gamit::CSerializer & __os, const message::gate::gatemsg::DictDictStringInt & __valDict, __DictDictStringInt_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        message::common::publicdef::__write(__os, __pair.second, message::common::publicdef::__DictStringInt_U__());
    }
}

// implementation of class SSignup
gamit::CAutoRun registSSignup(message::gate::gatemsg::SSignup::regist);
std::string message::gate::gatemsg::SSignup::_msgName("SSignup");

void message::gate::gatemsg::SSignup::regist()
{
    gamit::MessageBlock::registCreateFunc("SSignup", SSignup::create);
}

const message::gate::gatemsg::SSignupPtr message::gate::gatemsg::SSignup::create()
{
    return (new SSignup());
}

void message::gate::gatemsg::SSignup::__read(gamit::CSerializer & __is)
{
    __is.read(username);
    __is.read(nickname);
    __is.read(password);
    __is.read(sex);
}

void message::gate::gatemsg::SSignup::__write(gamit::CSerializer & __os) const
{
    __os.write(username);
    __os.write(nickname);
    __os.write(password);
    __os.write(sex);
}

const std::string & message::gate::gatemsg::SSignup::__name() const
{
    return _msgName;
}

// implementation of class SLogin
gamit::CAutoRun registSLogin(message::gate::gatemsg::SLogin::regist);
std::string message::gate::gatemsg::SLogin::_msgName("SLogin");

void message::gate::gatemsg::SLogin::regist()
{
    gamit::MessageBlock::registCreateFunc("SLogin", SLogin::create);
}

const message::gate::gatemsg::SLoginPtr message::gate::gatemsg::SLogin::create()
{
    return (new SLogin());
}

void message::gate::gatemsg::SLogin::__read(gamit::CSerializer & __is)
{
    __is.read(username);
    __is.read(password);
}

void message::gate::gatemsg::SLogin::__write(gamit::CSerializer & __os) const
{
    __os.write(username);
    __os.write(password);
}

const std::string & message::gate::gatemsg::SLogin::__name() const
{
    return _msgName;
}

// implementation of class SLoginReturn
gamit::CAutoRun registSLoginReturn(message::gate::gatemsg::SLoginReturn::regist);
std::string message::gate::gatemsg::SLoginReturn::_msgName("SLoginReturn");

void message::gate::gatemsg::SLoginReturn::regist()
{
    gamit::MessageBlock::registCreateFunc("SLoginReturn", SLoginReturn::create);
}

const message::gate::gatemsg::SLoginReturnPtr message::gate::gatemsg::SLoginReturn::create()
{
    return (new SLoginReturn());
}

void message::gate::gatemsg::SLoginReturn::__read(gamit::CSerializer & __is)
{
    __is.read(userId);
    __is.read(username);
    __is.read(nickname);
    __is.read(sessionKey);
    __is.read(sex);
}

void message::gate::gatemsg::SLoginReturn::__write(gamit::CSerializer & __os) const
{
    __os.write(userId);
    __os.write(username);
    __os.write(nickname);
    __os.write(sessionKey);
    __os.write(sex);
}

const std::string & message::gate::gatemsg::SLoginReturn::__name() const
{
    return _msgName;
}

// implementation of class SMessage
gamit::CAutoRun registSMessage(message::gate::gatemsg::SMessage::regist);
std::string message::gate::gatemsg::SMessage::_msgName("SMessage");

void message::gate::gatemsg::SMessage::regist()
{
    gamit::MessageBlock::registCreateFunc("SMessage", SMessage::create);
}

const message::gate::gatemsg::SMessagePtr message::gate::gatemsg::SMessage::create()
{
    return (new SMessage());
}

void message::gate::gatemsg::SMessage::__read(gamit::CSerializer & __is)
{
    __is.read(var1);
    __is.read(var2);
    __is.read(var3);
    __is.read(var4);
    __is.read(var5);
    __is.read(var6);
    __is.read(var7);
    message::common::publicdef::__read(__is, intList, message::common::publicdef::__SeqInt_U__());
    message::common::publicdef::__read(__is, dictStrInt, message::common::publicdef::__DictStringInt_U__());
}

void message::gate::gatemsg::SMessage::__write(gamit::CSerializer & __os) const
{
    __os.write(var1);
    __os.write(var2);
    __os.write(var3);
    __os.write(var4);
    __os.write(var5);
    __os.write(var6);
    __os.write(var7);
    message::common::publicdef::__write(__os, intList, message::common::publicdef::__SeqInt_U__());
    message::common::publicdef::__write(__os, dictStrInt, message::common::publicdef::__DictStringInt_U__());
}

const std::string & message::gate::gatemsg::SMessage::__name() const
{
    return _msgName;
}

void message::gate::gatemsg::__read(gamit::CSerializer & __is, message::gate::gatemsg::SeqMessage & __valList, __SeqMessage_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        message::gate::gatemsg::SMessage __val;
        __val.__read(__is);
        __valList.push_back(__val);
    }
}

void message::gate::gatemsg::__write(gamit::CSerializer & __os, const message::gate::gatemsg::SeqMessage & __valList, __SeqMessage_U__)
{
    __os.writeSize(__valList.size());
    for (auto __val: __valList)
    {
        __val.__write(__os);
    }
}

void message::gate::gatemsg::__read(gamit::CSerializer & __is, message::gate::gatemsg::DictMessage & __valDict, __DictMessage_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        int __key;
        message::gate::gatemsg::SMessage __val;
        __is.read(__key);
        __val.__read(__is);
        __valDict.insert({__key, __val});
    }
}

void message::gate::gatemsg::__write(gamit::CSerializer & __os, const message::gate::gatemsg::DictMessage & __valDict, __DictMessage_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __pair.second.__write(__os);
    }
}


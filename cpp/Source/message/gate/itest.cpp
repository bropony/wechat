/*
* @filename itest.cpp
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#include <message/gate/itest.h>

void message::gate::itest::__read(gamit::CSerializer & __is, message::gate::itest::DictStrMessage & __valDict, __DictStrMessage_U__)
{
    int __size = 0;
    __is.read(__size);
    for (int i = 0; i < __size; ++i)
    {
        std::string __key;
        message::gate::gatemsg::SMessage __val;
        __is.read(__key);
        __val.__read(__is);
        __valDict.insert({__key, __val});
    }
}

void message::gate::itest::__write(gamit::CSerializer & __os, const message::gate::itest::DictStrMessage & __valDict, __DictStrMessage_U__)
{
    __os.writeSize(__valDict.size());
    for (auto __pair: __valDict)
    {
        __os.write(__pair.first);
        __pair.second.__write(__os);
    }
}

void message::gate::itest::ITest_getIntList_Response::__onResponse(gamit::CSerializer & __is)
{
    message::common::publicdef::SeqInt intList;
    message::common::publicdef::__read(__is, intList, message::common::publicdef::__SeqInt_U__());
    onResponse(intList);
}

void message::gate::itest::ITest_getIntList_Response::__onError(gamit::CSerializer & __is)
{
    std::string __what;
    __is.read(__what);
    int __code;
    __is.read(__code);
    onError(__what, __code);
}

void message::gate::itest::ITest_getIntList_Response::__onTimeout()
{
    onTimeout();
}

void message::gate::itest::ITest_getDictIntString_Response::__onResponse(gamit::CSerializer & __is)
{
    message::common::publicdef::DictIntString intStrMap;
    message::common::publicdef::__read(__is, intStrMap, message::common::publicdef::__DictIntString_U__());
    onResponse(intStrMap);
}

void message::gate::itest::ITest_getDictIntString_Response::__onError(gamit::CSerializer & __is)
{
    std::string __what;
    __is.read(__what);
    int __code;
    __is.read(__code);
    onError(__what, __code);
}

void message::gate::itest::ITest_getDictIntString_Response::__onTimeout()
{
    onTimeout();
}

void message::gate::itest::ITest_getFloatList_Response::__onResponse(gamit::CSerializer & __is)
{
    message::common::publicdef::SeqFloat floatList;
    message::common::publicdef::__read(__is, floatList, message::common::publicdef::__SeqFloat_U__());
    onResponse(floatList);
}

void message::gate::itest::ITest_getFloatList_Response::__onError(gamit::CSerializer & __is)
{
    std::string __what;
    __is.read(__what);
    int __code;
    __is.read(__code);
    onError(__what, __code);
}

void message::gate::itest::ITest_getFloatList_Response::__onTimeout()
{
    onTimeout();
}

void message::gate::itest::ITest_signup_Response::__onResponse(gamit::CSerializer & __is)
{
    message::gate::gatemsg::SLoginReturn loginReturn;
    loginReturn.__read(__is);
    onResponse(loginReturn);
}

void message::gate::itest::ITest_signup_Response::__onError(gamit::CSerializer & __is)
{
    std::string __what;
    __is.read(__what);
    int __code;
    __is.read(__code);
    onError(__what, __code);
}

void message::gate::itest::ITest_signup_Response::__onTimeout()
{
    onTimeout();
}

std::string message::gate::itest::ITest::__proxyName("ITest");

void message::gate::itest::ITest::getIntList(const ITest_getIntList_ResponsePtr & __cb, int size)
{
    static std::string __methodName = "getIntList";

    gamit::CSerializer __os;
    __os.startToWrite();

    __os.write(int(gamit::ERmiType::RmiCall));
    __os.write(__proxyName);
    __os.write(__methodName);

    int __msgId = __getMsgId();
    __os.write(__msgId);
    __cb->setMsgId(__msgId);

    __os.write(size);

    invoke(__os, __cb);
}

void message::gate::itest::ITest::getDictIntString(const ITest_getDictIntString_ResponsePtr & __cb, int size)
{
    static std::string __methodName = "getDictIntString";

    gamit::CSerializer __os;
    __os.startToWrite();

    __os.write(int(gamit::ERmiType::RmiCall));
    __os.write(__proxyName);
    __os.write(__methodName);

    int __msgId = __getMsgId();
    __os.write(__msgId);
    __cb->setMsgId(__msgId);

    __os.write(size);

    invoke(__os, __cb);
}

void message::gate::itest::ITest::getFloatList(const ITest_getFloatList_ResponsePtr & __cb, int size)
{
    static std::string __methodName = "getFloatList";

    gamit::CSerializer __os;
    __os.startToWrite();

    __os.write(int(gamit::ERmiType::RmiCall));
    __os.write(__proxyName);
    __os.write(__methodName);

    int __msgId = __getMsgId();
    __os.write(__msgId);
    __cb->setMsgId(__msgId);

    __os.write(size);

    invoke(__os, __cb);
}

void message::gate::itest::ITest::signup(const ITest_signup_ResponsePtr & __cb, const message::gate::gatemsg::SSignup & signup)
{
    static std::string __methodName = "signup";

    gamit::CSerializer __os;
    __os.startToWrite();

    __os.write(int(gamit::ERmiType::RmiCall));
    __os.write(__proxyName);
    __os.write(__methodName);

    int __msgId = __getMsgId();
    __os.write(__msgId);
    __cb->setMsgId(__msgId);

    signup.__write(__os);

    invoke(__os, __cb);
}


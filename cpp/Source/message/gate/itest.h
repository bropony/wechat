/*
* @filename itest.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_GATE_ITEST_H__
#define __MESSAGE_GATE_ITEST_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>
#include <message/common/publicdef.h>
#include <message/gate/gatemsg.h>

namespace message{
    namespace gate{
        namespace itest{

            // DictStrMessage
            typedef std::map< std::string, message::gate::gatemsg::SMessage > DictStrMessage;
            class __DictStrMessage_U__{};
            void __read(gamit::CSerializer & __is, DictStrMessage & __valDict, __DictStrMessage_U__);
            void __write(gamit::CSerializer & __os, const DictStrMessage &__valDict, __DictStrMessage_U__);

            // ITest_getIntList_Response
            class ITest_getIntList_Response: public gamit::CRmiResponseBase
            {
                virtual void __onResponse(gamit::CSerializer & __is);
                virtual void __onError(gamit::CSerializer & __is);
                virtual void __onTimeout();

                virtual void onResponse(const message::common::publicdef::SeqInt & intList) = 0;
                virtual void onError(const std::string & what, int code) = 0;
                virtual void onTimeout() = 0;
            }; // class ITest_getIntList_Response
            typedef std::CSharedPtr<ITest_getIntList_Response> ITest_getIntList_ResponsePtr;

            // ITest_getDictIntString_Response
            class ITest_getDictIntString_Response: public gamit::CRmiResponseBase
            {
                virtual void __onResponse(gamit::CSerializer & __is);
                virtual void __onError(gamit::CSerializer & __is);
                virtual void __onTimeout();

                virtual void onResponse(const message::common::publicdef::DictIntString & intStrMap) = 0;
                virtual void onError(const std::string & what, int code) = 0;
                virtual void onTimeout() = 0;
            }; // class ITest_getDictIntString_Response
            typedef std::CSharedPtr<ITest_getDictIntString_Response> ITest_getDictIntString_ResponsePtr;

            // ITest_getFloatList_Response
            class ITest_getFloatList_Response: public gamit::CRmiResponseBase
            {
                virtual void __onResponse(gamit::CSerializer & __is);
                virtual void __onError(gamit::CSerializer & __is);
                virtual void __onTimeout();

                virtual void onResponse(const message::common::publicdef::SeqFloat & floatList) = 0;
                virtual void onError(const std::string & what, int code) = 0;
                virtual void onTimeout() = 0;
            }; // class ITest_getFloatList_Response
            typedef std::CSharedPtr<ITest_getFloatList_Response> ITest_getFloatList_ResponsePtr;

            // ITest_signup_Response
            class ITest_signup_Response: public gamit::CRmiResponseBase
            {
                virtual void __onResponse(gamit::CSerializer & __is);
                virtual void __onError(gamit::CSerializer & __is);
                virtual void __onTimeout();

                virtual void onResponse(const message::gate::gatemsg::SLoginReturn & loginReturn) = 0;
                virtual void onError(const std::string & what, int code) = 0;
                virtual void onTimeout() = 0;
            }; // class ITest_signup_Response
            typedef std::CSharedPtr<ITest_signup_Response> ITest_signup_ResponsePtr;

            // ITest
            class ITest: public gamit::CRmiProxyBase
            {
            public:
                void getIntList(const ITest_getIntList_ResponsePtr &, int size);
                void getDictIntString(const ITest_getDictIntString_ResponsePtr &, int size);
                void getFloatList(const ITest_getFloatList_ResponsePtr &, int size);
                void signup(const ITest_signup_ResponsePtr &, const message::gate::gatemsg::SSignup & signup);

            private:
                static std::string __proxyName;
            }; // class ITest
            typedef std::CSharedPtr<ITest> ITestPtr;

        }
    }
}

#endif //__MESSAGE_GATE_ITEST_H__

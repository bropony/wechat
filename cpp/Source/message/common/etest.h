/*
* @filename etest.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_COMMON_ETEST_H__
#define __MESSAGE_COMMON_ETEST_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>

namespace message{
    namespace common{
        namespace etest{

            // enum class EHelloWorld
            enum class EHelloWorld
            {
                Hello = 0,
                World = 1,
            };
            void read(gamit::CSerializer & __is, EHelloWorld & __val);
            void write(gamit::CSerializer & __os, EHelloWorld __val);

            //SHelloEnum
            class SHelloEnum;
            typedef std::CSharedPtr<SHelloEnum> SHelloEnumPtr;
            class SHelloEnum: public gamit::MessageBase
            {
            public:
                int age;
                std::string damn;
                message::common::etest::EHelloWorld greetType;

                static void regist();
                static const SHelloEnumPtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class SHelloEnum
            gamit::CAutoRun registSHelloEnum(SHelloEnum::regist);

        }
    }
}

#endif //__MESSAGE_COMMON_ETEST_H__

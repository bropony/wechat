/*
* @filename gatemsg.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_GATE_GATEMSG_H__
#define __MESSAGE_GATE_GATEMSG_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>
#include <message/common/publicdef.h>

namespace message{
    namespace gate{
        namespace gatemsg{

            // SeqSeqInt
            typedef std::vector< message::common::publicdef::SeqInt > SeqSeqInt;
            class __SeqSeqInt_U__{};
            void __read(gamit::CSerializer & __is, SeqSeqInt & __valList, __SeqSeqInt_U__);
            void __write(gamit::CSerializer & __os, const SeqSeqInt &__valList, __SeqSeqInt_U__);

            // SeqDictIntInt
            typedef std::vector< message::common::publicdef::DictIntInt > SeqDictIntInt;
            class __SeqDictIntInt_U__{};
            void __read(gamit::CSerializer & __is, SeqDictIntInt & __valList, __SeqDictIntInt_U__);
            void __write(gamit::CSerializer & __os, const SeqDictIntInt &__valList, __SeqDictIntInt_U__);

            // DictDictStringInt
            typedef std::map< int, message::common::publicdef::DictStringInt > DictDictStringInt;
            class __DictDictStringInt_U__{};
            void __read(gamit::CSerializer & __is, DictDictStringInt & __valDict, __DictDictStringInt_U__);
            void __write(gamit::CSerializer & __os, const DictDictStringInt &__valDict, __DictDictStringInt_U__);

            //SSignup
            class SSignup;
            typedef std::CSharedPtr<SSignup> SSignupPtr;
            class SSignup: public gamit::MessageBase
            {
            public:
                std::string username;
                std::string nickname;
                std::string password;
                int sex;

                static void regist();
                static const SSignupPtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class SSignup

            //SLogin
            class SLogin;
            typedef std::CSharedPtr<SLogin> SLoginPtr;
            class SLogin: public gamit::MessageBase
            {
            public:
                std::string username;
                std::string password;

                static void regist();
                static const SLoginPtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class SLogin

            //SLoginReturn
            class SLoginReturn;
            typedef std::CSharedPtr<SLoginReturn> SLoginReturnPtr;
            class SLoginReturn: public gamit::MessageBase
            {
            public:
                int userId;
                std::string username;
                std::string nickname;
                std::string sessionKey;
                int sex;

                static void regist();
                static const SLoginReturnPtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class SLoginReturn

            //SMessage
            class SMessage;
            typedef std::CSharedPtr<SMessage> SMessagePtr;
            class SMessage: public gamit::MessageBase
            {
            public:
                short var1;
                int var2;
                long64_t var3;
                float var4;
                double var5;
                std::string var6;
                gamit::CDateTime var7;
                message::common::publicdef::SeqInt intList;
                message::common::publicdef::DictStringInt dictStrInt;

                static void regist();
                static const SMessagePtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class SMessage

            // SeqMessage
            typedef std::vector< message::gate::gatemsg::SMessage > SeqMessage;
            class __SeqMessage_U__{};
            void __read(gamit::CSerializer & __is, SeqMessage & __valList, __SeqMessage_U__);
            void __write(gamit::CSerializer & __os, const SeqMessage &__valList, __SeqMessage_U__);

            // DictMessage
            typedef std::map< int, message::gate::gatemsg::SMessage > DictMessage;
            class __DictMessage_U__{};
            void __read(gamit::CSerializer & __is, DictMessage & __valDict, __DictMessage_U__);
            void __write(gamit::CSerializer & __os, const DictMessage &__valDict, __DictMessage_U__);

        }
    }
}

#endif //__MESSAGE_GATE_GATEMSG_H__

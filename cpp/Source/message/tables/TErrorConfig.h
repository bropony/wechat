/*
* @filename TErrorConfig.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_TABLES_TERRORCONFIG_H__
#define __MESSAGE_TABLES_TERRORCONFIG_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>

namespace message{
    namespace tables{
        namespace TErrorConfig{

            //TErrorConfig
            class TErrorConfig;
            typedef std::CSharedPtr<TErrorConfig> TErrorConfigPtr;
            class TErrorConfig: public gamit::MessageBase
            {
            public:
                int errorCode;
                std::string errorName;
                std::string errorStr;

                static void regist();
                static const TErrorConfigPtr create();

                virtual void __read(gamit::CSerializer & __is);
                virtual void __write(gamit::CSerializer & __os) const;
                virtual const std::string & __name() const;

            private:
                static std::string _msgName;
            }; // class TErrorConfig

            // SeqTErrorConfig
            typedef std::vector< message::tables::TErrorConfig::TErrorConfig > SeqTErrorConfig;
            class __SeqTErrorConfig_U__{};
            void __read(gamit::CSerializer & __is, SeqTErrorConfig & __valList, __SeqTErrorConfig_U__);
            void __write(gamit::CSerializer & __os, const SeqTErrorConfig &__valList, __SeqTErrorConfig_U__);

        }
    }
}

#endif //__MESSAGE_TABLES_TERRORCONFIG_H__

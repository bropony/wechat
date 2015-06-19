/*
* @filename publicdef.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#ifndef __MESSAGE_COMMON_PUBLICDEF_H__
#define __MESSAGE_COMMON_PUBLICDEF_H__

#include <map>
#include <vector>
#include <gamit/util/autorun.h>
#include <gamit/util/sharedptr.h>
#include <gamit/serialize/serializer.h>
#include <gamit/rmi/RmiCore.h>
#include <gamit/message/Message.h>

namespace message{
    namespace common{
        namespace publicdef{

            // SeqInt
            typedef std::vector< int > SeqInt;
            class __SeqInt_U__{};
            void __read(gamit::CSerializer & __is, SeqInt & __valList, __SeqInt_U__);
            void __write(gamit::CSerializer & __os, const SeqInt &__valList, __SeqInt_U__);

            // SeqLong
            typedef std::vector< long64_t > SeqLong;
            class __SeqLong_U__{};
            void __read(gamit::CSerializer & __is, SeqLong & __valList, __SeqLong_U__);
            void __write(gamit::CSerializer & __os, const SeqLong &__valList, __SeqLong_U__);

            // SeqString
            typedef std::vector< std::string > SeqString;
            class __SeqString_U__{};
            void __read(gamit::CSerializer & __is, SeqString & __valList, __SeqString_U__);
            void __write(gamit::CSerializer & __os, const SeqString &__valList, __SeqString_U__);

            // SeqFloat
            typedef std::vector< float > SeqFloat;
            class __SeqFloat_U__{};
            void __read(gamit::CSerializer & __is, SeqFloat & __valList, __SeqFloat_U__);
            void __write(gamit::CSerializer & __os, const SeqFloat &__valList, __SeqFloat_U__);

            // DictIntInt
            typedef std::map< int, int > DictIntInt;
            class __DictIntInt_U__{};
            void __read(gamit::CSerializer & __is, DictIntInt & __valDict, __DictIntInt_U__);
            void __write(gamit::CSerializer & __os, const DictIntInt &__valDict, __DictIntInt_U__);

            // DictIntString
            typedef std::map< int, std::string > DictIntString;
            class __DictIntString_U__{};
            void __read(gamit::CSerializer & __is, DictIntString & __valDict, __DictIntString_U__);
            void __write(gamit::CSerializer & __os, const DictIntString &__valDict, __DictIntString_U__);

            // DictStringInt
            typedef std::map< std::string, int > DictStringInt;
            class __DictStringInt_U__{};
            void __read(gamit::CSerializer & __is, DictStringInt & __valDict, __DictStringInt_U__);
            void __write(gamit::CSerializer & __os, const DictStringInt &__valDict, __DictStringInt_U__);

            // DictStringString
            typedef std::map< std::string, std::string > DictStringString;
            class __DictStringString_U__{};
            void __read(gamit::CSerializer & __is, DictStringString & __valDict, __DictStringString_U__);
            void __write(gamit::CSerializer & __os, const DictStringString &__valDict, __DictStringString_U__);

        }
    }
}

#endif //__MESSAGE_COMMON_PUBLICDEF_H__

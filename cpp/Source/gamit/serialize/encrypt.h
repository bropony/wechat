#ifndef __GAMIT_SERIALIZE_ENCRYPT_H__
#define __GAMIT_SERIALIZE_ENCRYPT_H__

#include <string>
#include <gamit/def/types.h>

namespace gamit
{
	class CEncrypto
	{
	public:
		static void simpleEncrypt(std::string & src);
		static void simpleDecrypt(std::string & src);
		
	private:
		static void __mask(std::string & src);
		static void __encrypt(std::string & src);
		static void __decrypt(std::string & src);

		static byte_t _mask;
	};
}

#endif
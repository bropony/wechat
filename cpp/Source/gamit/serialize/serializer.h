#ifndef __CDF_SIMPLE_SERIALIZER_H__
#define __CDF_SIMPLE_SERIALIZER_H__

#include <string>
#include <vector>
#include "gamit/util/datetime.h"
#include "gamit/util/endian.h"

namespace gamit
{
	enum class ERmiType
	{
		RmiCall = 1,
		RmiResponse = 2,
		MessageBlock = 3,
		RmiException = 4,
	};

	class CSerializer
	{
	public:
		CSerializer();
		CSerializer(const std::string & data);
		~CSerializer(){}

		//get buffer
		inline const std::string & getBuffer() const { return _buffer; }
		inline std::string & getBuffer(){ return _buffer; }

		//prepare
		void startToRead();
		void startToWrite();

		template <typename T>
		void write(const std::vector<T> & v)
		{
			writeSize(v.size());

			for (auto a : v)
			{
				write(a);
			}
		}

		//size
		void writeSize(const unsigned size);
		void readSize(unsigned & size);

		//byte
		void write(const byte_t b);
		void write(const byte_t * src, unsigned len);
		void read(byte_t & b);
		void read(std::vector<byte_t> & v);
		void read(byte_t* dst, unsigned len);

		//bool
		void write(const bool b);
		void read(bool & b);
		void read(std::vector<bool> & v);

		//short
		void write(const short s);
		void read(short & s);
		void read(std::vector<short> & v);

		//int
		void write(const int i);
		void read(int & i);
		void read(std::vector<int> & v);

		//long
		void write(const long64_t l);
		void read(long64_t & l);
		void read(std::vector<long64_t> & v);

		//float
		void write(const float f);
		void read(float & f);
		void read(std::vector<float> & v);

		//double
		void write(const double d);
		void read(double & d);
		void read(std::vector<double> & v);

		//date
		void write(const CDateTime & dt);
		void read(CDateTime & dt);
		void read(std::vector<CDateTime> & v);

		//string
		void write(const std::string & s);
		void read(std::string & s);
		void read(std::vector<std::string> & v);

	private:
		CSerializer(const CSerializer &);
		CSerializer & operator=(const CSerializer &);

		template <typename T>
		void _writeT(const T & v, unsigned len)
		{
			auto val = v;
#ifndef G_LITTLE_ENDIAN
			val = endian(val);
#endif

			byte_t * src = (byte_t*)&val;
			write(src, len);
		}

		template <typename T>
		void _readT(T & res, unsigned len)
		{
			byte_t * dst = (byte_t *)&res;

			read(dst, len);

#ifndef CDF_LITTLE_ENDIAN
			res = endian(res);
#endif
		}

	public:
		void encrypt();
		void decrypt();

	private:
		bool _hasStartedWriting;
		bool _hasStartedReading;
		std::string _buffer;
		unsigned _readPos;

		static byte_t VERSION;
	};
}

#endif
#include "serializer.h"
#include "serializeexception.h"

using namespace gamit;

static unsigned SIZE_OF_BYTE = 1;
static unsigned SIZE_OF_SHORT = 2;
static unsigned SIZE_OF_INT = 4;
static unsigned SIZE_OF_LONG = 8;
static unsigned SIZE_OF_FLOAT = 4;
static unsigned SIZE_OF_DOUBLE = 8;

byte_t CSerializer::VERSION = 1;

CSerializer::CSerializer()
:_hasStartedReading(false)
, _hasStartedWriting(false)
, _buffer()
, _readPos(0)
{

}

CSerializer::CSerializer(const std::string & data)
:_hasStartedReading(false)
, _hasStartedWriting(false)
, _buffer(data)
, _readPos(0)
{

}

//prepare
void CSerializer::startToRead()
{
	if (_hasStartedReading)
	{
		return;
	}

	byte_t version;
	read(version);
	if (version != VERSION)
	{
		G_THROW_EXCEPTION(CSerializeException, "SERIALIZE VERSION ERROR");
	}

	_hasStartedReading = true;
}

void CSerializer::startToWrite()
{
	if (_hasStartedWriting)
	{
		return;
	}

	write(VERSION);
	_hasStartedWriting = true;
}

void CSerializer::writeSize(const unsigned size)
{
	write(int(size));
}

void CSerializer::readSize(unsigned & size)
{
	int res = 0;
	read(res);

	size = unsigned(res);
}


//byte
void CSerializer::write(const byte_t b)
{
	_buffer.push_back(b);
}

void CSerializer::write(const byte_t * src, unsigned len)
{
	for (unsigned i = 0; i < len; ++i)
	{
		write(src[i]);
	}
}

void CSerializer::read(byte_t & b)
{
	if (_readPos > _buffer.size())
	{
		throw CSerializeException("SerializeError");
	}

	b = _buffer[_readPos];
	_readPos += SIZE_OF_BYTE;
}

void CSerializer::read(std::vector<byte_t> & v)
{
	unsigned size = 0;
	readSize(size);

	if (size + _readPos > _buffer.size())
	{
		throw CSerializeException("SerializeError");
	}

	for (unsigned i = 0; i < size; ++i)
	{
		byte_t val = 0;
		read(val);
		v.push_back(val);
	}
}

void CSerializer::read(byte_t* dst, unsigned len)
{
	if (len + _readPos > _buffer.size())
	{
		throw CSerializeException("SerializeError");
	}

	byte_t * src = (byte_t *)(_buffer.c_str() + _readPos);
	for (unsigned i = 0; i < len; ++i)
	{
		dst[i] = src[i];
	}

	_readPos += len;
}

//bool
void CSerializer::write(const bool b)
{
	byte_t val = b ? 1 : 0;
	write(val);
}

void CSerializer::read(bool & b)
{
	byte_t res = 0;
	read(res);

	b = (res != 0);
}

void CSerializer::read(std::vector<bool> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		bool val = false;
		read(val);
		v.push_back(val);
	}
}

//short
void CSerializer::write(const short s)
{
	_writeT(s, SIZE_OF_SHORT);
}

void CSerializer::read(short & s)
{
	_readT(s, SIZE_OF_SHORT);
}

void CSerializer::read(std::vector<short> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		short val = 0;
		read(val);
		v.push_back(val);
	}
}

//int
void CSerializer::write(const int i)
{
	_writeT(i, SIZE_OF_INT);
}

void CSerializer::read(int & i)
{
	_readT(i, SIZE_OF_INT);
}

void CSerializer::read(std::vector<int> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		int val = 0;
		read(val);
		v.push_back(val);
	}
}

//long
void CSerializer::write(const long64_t l)
{
	_writeT(l, SIZE_OF_LONG);
}

void CSerializer::read(long64_t & l)
{
	_readT(l, SIZE_OF_LONG);
}

void CSerializer::read(std::vector<long64_t> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		long64_t val = 0;
		read(val);
		v.push_back(val);
	}
}

//float
void CSerializer::write(const float f)
{
	_writeT(f, SIZE_OF_FLOAT);
}

void CSerializer::read(float & f)
{
	_readT(f, SIZE_OF_FLOAT);
}

void CSerializer::read(std::vector<float> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		float val = 0;
		read(val);
		v.push_back(val);
	}
}

//double
void CSerializer::write(const double d)
{
	_writeT(d, SIZE_OF_DOUBLE);
}
void CSerializer::read(double & d)
{
	_readT(d, SIZE_OF_DOUBLE);
}

void CSerializer::read(std::vector<double> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		double val = 0;
		read(val);
		v.push_back(val);
	}
}

//date
void CSerializer::write(const CDateTime & dt)
{
	write(dt.getTotalSecond());
}

void CSerializer::read(CDateTime & dt)
{
	long64_t mills = 0;
	read(mills);

	dt = CDateTime(mills * 1000);
}

void CSerializer::read(std::vector<CDateTime> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		CDateTime val;
		read(val);
		v.push_back(val);
	}
}

//string
void CSerializer::write(const std::string & s)
{
	auto size = s.size();
	writeSize(size);

	if (size == 0)
	{
		return;
	}

	const byte_t * src = (byte_t *)s.c_str();
	write(src, size);
}

void CSerializer::read(std::string & s)
{
	unsigned size = 0;
	readSize(size);

	if (size == 0)
	{
		return;
	}

	for (unsigned i = 0; i < size; ++i)
	{
		byte_t b = 0;
		read(b);
		s.push_back(b);
	}
}

void CSerializer::read(std::vector<std::string> & v)
{
	unsigned size = 0;
	readSize(size);

	for (unsigned i = 0; i < size; ++i)
	{
		std::string val;
		read(val);
		v.push_back(val);
	}
}

void CSerializer::encrypt()
{
	byte_t mask = 108;

	if (_buffer.empty())
	{
		return;
	}

	unsigned maxIdx = _buffer.size() - 1;

	for (unsigned i = 0; i <= maxIdx; i += 2)
	{
		if (i == maxIdx)
		{
			_buffer[i] ^= mask;
			return;
		}

		byte_t bi = _buffer[i];
		byte_t bj = _buffer[i + 1];

		bi ^= mask;
		bj ^= mask;

		_buffer[i] = bj;
		_buffer[i + 1] = bi;
	}
}

void CSerializer::decrypt()
{
	encrypt();
}

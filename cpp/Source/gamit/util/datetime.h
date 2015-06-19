#ifndef	__GAMIT_UTIL_H__
#define __GAMIT_UTIL_H__

#include <exception>
#include <ctime>
#include <string>
#include <gamit/def/types.h>
#include <gamit/util/exception.h>

namespace gamit
{
	typedef struct tm cdf_tm;
	class CDateTimeException : public CException
	{
	public :
		CDateTimeException( const char * msg );
		~CDateTimeException();
	};

	class CDateTime;
	class CInterval;

#define G_DEFAULT_DATETIME_FORMAT "YYYY-MM-DD hh:mm:ss.nnn"
#define G_NORMAL_DATETIME_FORMAT "YYYY-MM-DD hh:mm:ss"
#define G_DEFAULT_INTERVAL_FORMAT "DD hh:mm:ss.nnn"

	class CDateTime
	{
	private:
		short _timeZone;

		short _showZone;

		long64_t _timeSpan;

		//time_t _time;
		cdf_tm* _tm;
	private :
		long getTimeZoneMills() const;

		bool asYMD(struct tm* time,unsigned long mills,
			const char ch,char* buf,int index,
			int count,int bufsize) const;

	public:
		void update();

		bool init(
			int year, int month, int day, int hour,
			int minute, int second,int millseconds,
			short timezone = 0);

		bool init( long64_t millseconds , short timezone = 0 );

	public:

		std::string asString(const char* format = G_DEFAULT_DATETIME_FORMAT) const;

		CDateTime();

		CDateTime(int year, int month, int day, int hour,
			int minute, int second,int millSeconds,
			short timezone = 0);

		CDateTime( long64_t millseconds , short timezone = 0 );

		CDateTime(const CDateTime& other);

		virtual ~CDateTime();

		int getYear() const;

		int getMonth() const;

		int getDay() const;

		int getHour() const;

		int getMinute() const;

		int getSecond() const;

		int getDayOfWeek() const;

		int getMillSecond() const;

		void clearMillSecond();

		int getTotalDay() const;

		long64_t getTotalMill() const;

		long64_t getTotalSecond() const;

		CInterval operator -(const CDateTime& other) const;

		CDateTime operator -(const CInterval& interval) const;

		CDateTime operator +(const CInterval& interval) const;

		CDateTime& operator =(const CDateTime& other);

		const CDateTime& operator -=(const CInterval& interval);

		const CDateTime& operator +=(const CInterval& interval);

		bool operator==(const CDateTime& other) const;

		bool operator !=(const CDateTime& other) const;

		bool operator <=(const CDateTime& other) const;

		bool operator <(const CDateTime& other) const;

		bool operator >(const CDateTime& other) const;

		bool operator >=(const CDateTime& other) const;

		void parse(const char* value, const char* format = G_DEFAULT_DATETIME_FORMAT);

		void setShowTimeZone(short timezone);

	public:
		static CDateTime getAbsDt();
		//static cdf::CLightLock& getLock();
		//static void updateThreadDt();
		//static CDateTime getThreadDt();

		static void setLocalTimeZone( int localTimeZone );

	private:
		const cdf_tm* getLocalTime() const;

		void clearTm();
		
		static CDateTime _lastDt;

		static int _localTimeZone;
	};

	class CInterval
	{
	public:
		const static CInterval _zero;
	private:
		friend class CDateTime;
		long64_t _timeSpan;

	private:
		bool asYMD(const char ch,char* buf,int index,int count,int bufsize) const;

	public:

		CInterval(int days, int hours, int minutes, int seconds,int millseconds);

		CInterval(const CInterval& other);

		CInterval( const int second , const int micro );

		CInterval(const long64_t millseconds);

		CInterval();

		int getDays() const;

		int getTotalSeconds() const;

		int getTotalMinutes() const;

		int getTotalHours() const;
		long64_t getTotalMills() const;

		int getSecondsOfDay() const;

		int getMinutesOfDay() const;

		int getHoursOfDay() const;

		int getMillsOfDay() const;

		CInterval operator -(const CInterval& other) const;

		CInterval operator +(const CInterval& other) const;

		const CInterval& operator -=(const CInterval& other);

		const CInterval& operator +=(const CInterval& other);

		bool operator ==(const CInterval& other) const;

		bool operator !=(const CInterval& other) const;

		bool operator <(const CInterval& other) const;

		bool operator <=(const CInterval& other) const;

		bool operator >(const CInterval& other) const;

		bool operator >=(const CInterval& other) const;

		void parse(const char* value,const char* format = G_DEFAULT_INTERVAL_FORMAT);

		std::string asString(const char* format = G_DEFAULT_INTERVAL_FORMAT) const;

	};

}
#endif

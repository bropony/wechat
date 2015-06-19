#ifndef __GAMIT_RMI_RMI_CORE_H__
#define __GAMIT_RMI_RMI_CORE_H__

#include <gamit/serialize/serializer.h>
#include <gamit/util/sharedptr.h>

namespace gamit
{
	//predeclarations
	class CConnectionOpenCallbackBase;
	typedef std::CSharedPtr<CConnectionOpenCallbackBase> CConnectionOpenCallbackBasePtr;

	class CRmiClientBase;
	typedef std::CSharedPtr<CRmiClientBase> CRmiClientBasePtr;

	class CRmiResponseBase;
	typedef std::CSharedPtr<CRmiResponseBase> CRmiResponseBasePtr;

	class CRmiProxyBase;
	typedef std::CSharedPtr<CRmiProxyBase> CRmiProxyBasePtr;

	// client connection callback
	class CConnectionOpenCallbackBase
	{
	public:
		virtual void onOpen() = 0;
	};

	// rmi client base
	class CRmiClientBase
	{
	public:
		virtual void onOpen() = 0;

		virtual void onClose() = 0;
		virtual void onMessage(const std::string & payload, bool isBinary) = 0;
		virtual void send(const CSerializer & __os) = 0;
		virtual void send(const std::string & payload, bool isBinary) = 0;

		virtual void start() = 0;
		virtual void stop() = 0;

		virtual void addResponse(const CRmiResponseBasePtr & cb) = 0;

		void setConnectionOpenCallback(const CConnectionOpenCallbackBasePtr & callback);

	protected:
		CConnectionOpenCallbackBasePtr _connectionOpenCallback;

	};

	// Rmi Call Response Base
	class CRmiResponseBase
	{
	public:
		CRmiResponseBase();
		virtual ~CRmiResponseBase(){}

		virtual void __onResponse(CSerializer & __is) = 0;
		virtual void __onError(CSerializer & __is) = 0;
		virtual void __onTimeout() = 0;

		void setMsgId(int msgId);
		int getMsgId();
		bool isExpired(long64_t mills);

	private:
		int _msgId;
		CDateTime _createDt;
	};

	// what an Rmi Proxy looks like
	class CRmiProxyBase
	{
	public:
		CRmiProxyBase() :_client(){}
		virtual ~CRmiProxyBase(){}

		void invoke(CSerializer & __os, const CRmiResponseBasePtr & __cb);
		void setClient(const CRmiClientBasePtr & client);

	public:
		static int __getMsgId();

	private:
		CRmiClientBasePtr _client;
		static int _msgIdBase;
	};
}

#endif
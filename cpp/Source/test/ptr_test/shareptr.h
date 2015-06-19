#ifndef __TEST_PTR_TEST_SHARE_PTR_H__
#define __TEST_PTR_TEST_SHARE_PTR_H__

#include <gamit/util/sharedptr.h>
#include <iostream>
#include <functional>
#include <map>

namespace Test
{
	class Base
	{
	public:
		Base() :value(){}
		virtual ~Base(){ std::cout << "~Base()" << std::endl; }
		void setVal(int val){ value = val; }

		virtual void show()
		{
			std::cout << "Base: " << value << std::endl;
		}

	protected:
		int value;
	};
	typedef std::CSharedPtr<Base> BasePtr;

	class Derived : public Base
	{
	public:
		Derived() :Base(){}
		virtual ~Derived(){ std::cout << "~Derived()" << std::endl; }

		virtual void show()
		{
			std::cout << "Derived: " << value << std::endl;
		}


	};
	typedef std::CSharedPtr<Derived> DerivedPtr;

	class Nothing
	{
	public:
		Nothing(int i)
		{
			std::cout << "Nothing: " << i << std::endl;
		}
	};
	typedef std::CSharedPtr<Nothing> NothingPtr;

	class CPtrTest
	{
	public:
		static void show(const BasePtr & ptr)
		{
			ptr->show();
		}

		static void hi()
		{
			std::cout << "hiiiiii" << std::endl;
		}

		static void runTest()
		{
			funcMap[1] = hi;
			funcMap[2] = hay;

			funcMap[1]();
			funcMap[2]();
		}

		static void hay()
		{
			std::cout << "hayyyyyy" << std::endl;
		}

		static std::map<int, std::function<void()> > funcMap;
	};
	std::map<int, std::function<void()> > CPtrTest::funcMap;
}

#endif
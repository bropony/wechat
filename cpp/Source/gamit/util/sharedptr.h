#ifndef __GAMIT_UTIL_CSharedPtr_H__
#define __GAMIT_UTIL_CSharedPtr_H__

#include <memory>
#include <iostream>

namespace std
{
	template<class _Ty>
	class CSharedPtr
		: public _Ptr_base<_Ty>
	{	// class for reference counted resource management
	public:
		typedef CSharedPtr<_Ty> _Myt;
		typedef _Ptr_base<_Ty> _Mybase;

		CSharedPtr() _NOEXCEPT
		{	// construct empty CSharedPtr
		}

		template<class _Ux>
		CSharedPtr(_Ux *_Px)
		{	// construct CSharedPtr object that owns _Px
			_Resetp(_Px);
		}

		template<class _Ux,
		class _Dx>
			CSharedPtr(_Ux *_Px, _Dx _Dt)
		{	// construct with _Px, deleter
				_Resetp(_Px, _Dt);
			}

		CSharedPtr(nullptr_t)
		{	// construct empty CSharedPtr
		}

		template<class _Dx>
		CSharedPtr(nullptr_t, _Dx _Dt)
		{	// construct with nullptr, deleter
			_Resetp((_Ty *)0, _Dt);
		}

		template<class _Dx,
		class _Alloc>
			CSharedPtr(nullptr_t, _Dx _Dt, _Alloc _Ax)
		{	// construct with nullptr, deleter, allocator
				_Resetp((_Ty *)0, _Dt, _Ax);
			}

		template<class _Ux,
		class _Dx,
		class _Alloc>
			CSharedPtr(_Ux *_Px, _Dx _Dt, _Alloc _Ax)
		{	// construct with _Px, deleter, allocator
				_Resetp(_Px, _Dt, _Ax);
			}

		template<class _Ty2>
		CSharedPtr(const CSharedPtr<_Ty2>& _Right, _Ty *_Px) _NOEXCEPT
		{	// construct CSharedPtr object that aliases _Right
			this->_Reset(_Px, _Right);
		}

		CSharedPtr(const _Myt& _Other) _NOEXCEPT
		{	// construct CSharedPtr object that owns same resource as _Other
			this->_Reset(_Other);
		}

		template<class _Ty2,
		class = typename enable_if<is_convertible<_Ty2 *, _Ty *>::value,
			void>::type>
			CSharedPtr(const CSharedPtr<_Ty2>& _Other) _NOEXCEPT
		{	// construct CSharedPtr object that owns same resource as _Other
			this->_Reset(_Other);
		}

		template<class _Ty2>
		explicit CSharedPtr(const weak_ptr<_Ty2>& _Other,
			bool _Throw = true)
		{	// construct CSharedPtr object that owns resource *_Other
			this->_Reset(_Other, _Throw);
		}

		template<class _Ty2>
		CSharedPtr(auto_ptr<_Ty2>&& _Other)
		{	// construct CSharedPtr object that owns *_Other.get()
			this->_Reset(_STD move(_Other));
		}

		template<class _Ty2>
		CSharedPtr(const CSharedPtr<_Ty2>& _Other, const _Static_tag& _Tag)
		{	// construct CSharedPtr object for static_pointer_cast
			this->_Reset(_Other, _Tag);
		}

		template<class _Ty2>
		CSharedPtr(const CSharedPtr<_Ty2>& _Other, const _Const_tag& _Tag)
		{	// construct CSharedPtr object for const_pointer_cast
			this->_Reset(_Other, _Tag);
		}

		template<class _Ty2>
		CSharedPtr(const CSharedPtr<_Ty2>& _Other, const _Dynamic_tag& _Tag)
		{	// construct CSharedPtr object for dynamic_pointer_cast
			this->_Reset(_Other, _Tag);
		}

		CSharedPtr(_Myt&& _Right) _NOEXCEPT
			: _Mybase(_STD forward<_Myt>(_Right))
		{	// construct CSharedPtr object that takes resource from _Right
			}

		template<class _Ty2,
		class = typename enable_if<is_convertible<_Ty2 *, _Ty *>::value,
			void>::type>
			CSharedPtr(CSharedPtr<_Ty2>&& _Right) _NOEXCEPT
			: _Mybase(_STD forward<CSharedPtr<_Ty2> >(_Right))
		{	// construct CSharedPtr object that takes resource from _Right
			}

		template<class _Ux,
		class _Dx>
			CSharedPtr(unique_ptr<_Ux, _Dx>&& _Right)
		{	// construct from unique_ptr
				_Resetp(_Right.release(), _Right.get_deleter());
			}

		template<class _Ux,
		class _Dx>
			_Myt& operator=(unique_ptr<_Ux, _Dx>&& _Right)
		{	// move from unique_ptr
				CSharedPtr(_STD move(_Right)).swap(*this);
				return (*this);
			}

		_Myt& operator=(_Myt&& _Right) _NOEXCEPT
		{	// construct CSharedPtr object that takes resource from _Right
			CSharedPtr(_STD move(_Right)).swap(*this);
			return (*this);
		}

		template<class _Ty2>
		_Myt& operator=(CSharedPtr<_Ty2>&& _Right) _NOEXCEPT
		{	// construct CSharedPtr object that takes resource from _Right
			CSharedPtr(_STD move(_Right)).swap(*this);
			return (*this);
		}

		~CSharedPtr() _NOEXCEPT
		{	// release resource
			this->_Decref();
		}

		_Myt& operator=(const _Myt& _Right) _NOEXCEPT
		{	// assign shared ownership of resource owned by _Right
			CSharedPtr(_Right).swap(*this);
			return (*this);
		}

		template<class _Ty2>
		_Myt& operator=(const CSharedPtr<_Ty2>& _Right) _NOEXCEPT
		{	// assign shared ownership of resource owned by _Right
			CSharedPtr(_Right).swap(*this);
			return (*this);
		}

		template<class _Ty2>
		_Myt& operator=(auto_ptr<_Ty2>&& _Right)
		{	// assign ownership of resource pointed to by _Right
			CSharedPtr(_STD move(_Right)).swap(*this);
			return (*this);
		}

		void reset() _NOEXCEPT
		{	// release resource and convert to empty CSharedPtr object
			CSharedPtr().swap(*this);
		}

		template<class _Ux>
		void reset(_Ux *_Px)
		{	// release, take ownership of _Px
			CSharedPtr(_Px).swap(*this);
		}

		template<class _Ux,
		class _Dx>
			void reset(_Ux *_Px, _Dx _Dt)
		{	// release, take ownership of _Px, with deleter _Dt
				CSharedPtr(_Px, _Dt).swap(*this);
			}

		template<class _Ux,
		class _Dx,
		class _Alloc>
			void reset(_Ux *_Px, _Dx _Dt, _Alloc _Ax)
		{	// release, take ownership of _Px, with deleter _Dt, allocator _Ax
				CSharedPtr(_Px, _Dt, _Ax).swap(*this);
			}

		void swap(_Myt& _Other) _NOEXCEPT
		{	// swap pointers
			this->_Swap(_Other);
		}

		_Ty *get() const _NOEXCEPT
		{	// return pointer to resource
			return (this->_Get());
		}

		typename add_reference<_Ty>::type operator*() const _NOEXCEPT
		{	// return reference to resource
			return (*this->_Get());
		}

		_Ty *operator->() const _NOEXCEPT
		{	// return pointer to resource
			return (this->_Get());
		}

		bool unique() const _NOEXCEPT
		{	// return true if no other CSharedPtr object owns this resource
			return (this->use_count() == 1);
		}

		explicit operator bool() const _NOEXCEPT
		{	// test if CSharedPtr object owns no resource
			return (this->_Get() != 0);
		}

	private:
		template<class _Ux>
		void _Resetp(_Ux *_Px)
		{	// release, take ownership of _Px
			_TRY_BEGIN	// allocate control block and reset
				_Resetp0(_Px, new _Ref_count<_Ux>(_Px));
			_CATCH_ALL	// allocation failed, delete resource
				delete _Px;
			_RERAISE;
			_CATCH_END
		}

		template<class _Ux,
		class _Dx>
			void _Resetp(_Ux *_Px, _Dx _Dt)
		{	// release, take ownership of _Px, deleter _Dt
				_TRY_BEGIN	// allocate control block and reset
					_Resetp0(_Px, new _Ref_count_del<_Ux, _Dx>(_Px, _Dt));
				_CATCH_ALL	// allocation failed, delete resource
					_Dt(_Px);
				_RERAISE;
				_CATCH_END
			}

		template<class _Ux,
		class _Dx,
		class _Alloc>
			void _Resetp(_Ux *_Px, _Dx _Dt, _Alloc _Ax)
		{	// release, take ownership of _Px, deleter _Dt, allocator _Ax
				typedef _Ref_count_del_alloc<_Ux, _Dx, _Alloc> _Refd;
				typename _Alloc::template rebind<_Refd>::other _Al = _Ax;

				_TRY_BEGIN	// allocate control block and reset
					_Refd *_Ptr = _Al.allocate(1);
				::new (_Ptr)_Refd(_Px, _Dt, _Al);
				_Resetp0(_Px, _Ptr);
				_CATCH_ALL	// allocation failed, delete resource
					_Dt(_Px);
				_RERAISE;
				_CATCH_END
			}

	public:
		template<class _Ux>
		void _Resetp0(_Ux *_Px, _Ref_count_base *_Rx)
		{	// release resource and take ownership of _Px
			this->_Reset0(_Px, _Rx);
			_Enable_shared(_Px, _Rx);
		}

		template<class _Ty2>
		static CSharedPtr<_Ty>
			dynamicCast(const CSharedPtr<_Ty2>& _Other) _NOEXCEPT
		{	// return shared_ptr object holding dynamic_cast<_Ty1 *>(_Other.get())
			return (CSharedPtr<_Ty>(_Other, _Dynamic_tag()));
		}

		template<class _Ty2>
		static const CSharedPtr<_Ty> dynamicCast(const _Ty2 * ptr)
		{
			return CSharedPtr<_Ty>(dynamic_cast<_Ty *>(ptr));
		}
	};

	template<class _Ty1, class _Ty2>
	static bool operator==(const CSharedPtr<_Ty1> & _Left, const CSharedPtr<_Ty2> & _Right)
	{
		return (_Left.get() == _Right.get());
	}

	template<class _Ty1, class _Ty2>
	static bool operator!=(const CSharedPtr<_Ty1> & _Left, const CSharedPtr<_Ty2> & _Right)
	{
		return (_Left.get() != _Right.get());
	}

	template<class _Ty>
	static bool operator==(const CSharedPtr<_Ty> & _Left, const void * _Right)
	{
		return (_Left.get() == _Right);
	}

	template<class _Ty>
	static bool operator!=(const CSharedPtr<_Ty> & _Left, const void * _Right)
	{
		return (_Left.get() != _Right);
	}

	template<class _Ty>
	static bool operator==(const void * _Left, const CSharedPtr<_Ty> & _Right)
	{
		return (_Left == _Right.get());
	}

	template<class _Ty>
	static bool operator!=(const void * _Left, const CSharedPtr<_Ty> & _Right)
	{
		return (_Left != _Right.get());
	}
}

#endif
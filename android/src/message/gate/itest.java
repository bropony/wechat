/*
* @filename itest.java
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

package message.gate;


import java.util.Date;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;

import rmi.Serializer;
import rmi.MessageBlock;
import rmi.RmiCore;
import rmi.ProxyManager;
import rmi.RmiManager;
import message.common.publicdef;
import message.gate.gatemsg;


public class itest
{
    // Dict DictStrMessage
    public static class DictStrMessage
    {
        private Map<String, gatemsg.SMessage> __map;

        public DictStrMessage()
        {
            __map = new HashMap<String, gatemsg.SMessage>();
        }

        public Map<String, gatemsg.SMessage> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                gatemsg.SMessage __val = new gatemsg.SMessage();
                __val.__read(__is);
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<String> __keySet = __map.keySet();
            Iterator<String> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                String __key = __it.next();
                __os.write(__key);
                gatemsg.SMessage __val = __map.get(__key);
                __val.__write(__os);
            }
        }

    }

    // Reponse ITest_getIntList_response
    public static abstract class ITest_getIntList_response extends RmiCore.RmiResponseBase
    {
        public ITest_getIntList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicdef.SeqInt intList = new publicdef.SeqInt();
            intList.__read(__is);

            onResponse(intList);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(publicdef.SeqInt intList);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITest_getDictIntString_response
    public static abstract class ITest_getDictIntString_response extends RmiCore.RmiResponseBase
    {
        public ITest_getDictIntString_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicdef.DictIntString intStrMap = new publicdef.DictIntString();
            intStrMap.__read(__is);

            onResponse(intStrMap);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(publicdef.DictIntString intStrMap);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITest_getFloatList_response
    public static abstract class ITest_getFloatList_response extends RmiCore.RmiResponseBase
    {
        public ITest_getFloatList_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            publicdef.SeqFloat floatList = new publicdef.SeqFloat();
            floatList.__read(__is);
            int dummy = 0;
            dummy = __is.read(dummy);

            onResponse(floatList, dummy);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(publicdef.SeqFloat floatList, int dummy);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITest_signup_response
    public static abstract class ITest_signup_response extends RmiCore.RmiResponseBase
    {
        public ITest_signup_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            gatemsg.SLoginReturn loginReturn = new gatemsg.SLoginReturn();
            loginReturn.__read(__is);

            onResponse(loginReturn);
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse(gatemsg.SLoginReturn loginReturn);
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Reponse ITest_doNothing_response
    public static abstract class ITest_doNothing_response extends RmiCore.RmiResponseBase
    {
        public ITest_doNothing_response()
        {
            super();
        }

        @Override
        public void __onResponse(Serializer __is)
        {
            onResponse();
        }

        @Override
        public void __onError(String what, int code)
        {
            onError(what, code);
        }

        @Override
        public void __onTimeout()
        {
            onTimeout();
        }

        public abstract void onResponse();
        public abstract void onError(String what, int code);
        public abstract void onTimeout();
    }

    // Proxy ITestProxy
    public static class ITestProxy extends RmiCore.RmiProxyBase
    {
        public static void __regist(){
            // regist proxy at startup...
            ProxyManager.instance().addProxy(new ITestProxy());
        }

        public ITestProxy()
        {
            super("ITest");
        }

        public void getIntList(ITest_getIntList_response __response, int size)        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getIntList"));

            int __msgId = MessageBlock.getMsgId();
            __response.setMsgId(__msgId);
            __os.write(__msgId);

            __os.write(size);

            RmiManager.instance().invoke(__response, __os);
        }

        public void getDictIntString(ITest_getDictIntString_response __response, int size)        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getDictIntString"));

            int __msgId = MessageBlock.getMsgId();
            __response.setMsgId(__msgId);
            __os.write(__msgId);

            __os.write(size);

            RmiManager.instance().invoke(__response, __os);
        }

        public void getFloatList(ITest_getFloatList_response __response, int size)        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("getFloatList"));

            int __msgId = MessageBlock.getMsgId();
            __response.setMsgId(__msgId);
            __os.write(__msgId);

            __os.write(size);

            RmiManager.instance().invoke(__response, __os);
        }

        public void signup(ITest_signup_response __response, gatemsg.SSignup signup)        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("signup"));

            int __msgId = MessageBlock.getMsgId();
            __response.setMsgId(__msgId);
            __os.write(__msgId);

            signup.__write(__os);

            RmiManager.instance().invoke(__response, __os);
        }

        public void doNothing(ITest_doNothing_response __response)        {
            Serializer __os = new Serializer();
            __os.startToWrite();
            __os.write(Serializer.RmiDataCall);
            __os.write(getName());
            __os.write(new String("doNothing"));

            int __msgId = MessageBlock.getMsgId();
            __response.setMsgId(__msgId);
            __os.write(__msgId);
            RmiManager.instance().invoke(__response, __os);
        }

    }

}


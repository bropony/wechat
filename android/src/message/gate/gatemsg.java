/*
* @filename gatemsg.java
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
import rmi.RmiCore;
import rmi.MessageBlock;
import message.common.publicdef;


public class gatemsg
{
    // List SeqSeqInt
    public static class SeqSeqInt
    {
        private publicdef.SeqInt[] __array;

        public SeqSeqInt()
        {
            __array = null;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new publicdef.SeqInt[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                publicdef.SeqInt __val = new publicdef.SeqInt();
                __val.__read(__is);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __array[i].__write(__os);
            }
        }

    }

    // List SeqDictIntInt
    public static class SeqDictIntInt
    {
        private publicdef.DictIntInt[] __array;

        public SeqDictIntInt()
        {
            __array = null;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new publicdef.DictIntInt[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                publicdef.DictIntInt __val = new publicdef.DictIntInt();
                __val.__read(__is);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __array[i].__write(__os);
            }
        }

    }

    // Dict DictDictStringInt
    public static class DictDictStringInt
    {
        private Map<Integer, publicdef.DictStringInt> __map;

        public DictDictStringInt()
        {
            __map = new HashMap<Integer, publicdef.DictStringInt>();
        }

        public Map<Integer, publicdef.DictStringInt> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                publicdef.DictStringInt __val = new publicdef.DictStringInt();
                __val.__read(__is);
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<Integer> __keySet = __map.keySet();
            Iterator<Integer> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                Integer __key = __it.next();
                __os.write(__key.intValue());
                publicdef.DictStringInt __val = __map.get(__key);
                __val.__write(__os);
            }
        }

    }

    // class SSignup
    public static class SSignup extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SSignup();
            }
        }

        static {
            MessageBlock.regist("SSignup", new AutoRegist());
        }

        public String username;
        public String nickname;
        public String password;
        public int sex;

        public SSignup()
        {
            username = "";
            nickname = "";
            password = "";
            sex = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            username = __is.read(username);
            nickname = __is.read(nickname);
            password = __is.read(password);
            sex = __is.read(sex);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(username);
            __os.write(nickname);
            __os.write(password);
            __os.write(sex);
        }
    } // end of class SSignup

    // class SLogin
    public static class SLogin extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SLogin();
            }
        }

        static {
            MessageBlock.regist("SLogin", new AutoRegist());
        }

        public String username;
        public String password;

        public SLogin()
        {
            username = "";
            password = "";
        }

        @Override
        public void __read(Serializer __is)
        {
            username = __is.read(username);
            password = __is.read(password);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(username);
            __os.write(password);
        }
    } // end of class SLogin

    // class SLoginReturn
    public static class SLoginReturn extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SLoginReturn();
            }
        }

        static {
            MessageBlock.regist("SLoginReturn", new AutoRegist());
        }

        public int userId;
        public String username;
        public String nickname;
        public String sessionKey;
        public int sex;

        public SLoginReturn()
        {
            userId = 0;
            username = "";
            nickname = "";
            sessionKey = "";
            sex = 0;
        }

        @Override
        public void __read(Serializer __is)
        {
            userId = __is.read(userId);
            username = __is.read(username);
            nickname = __is.read(nickname);
            sessionKey = __is.read(sessionKey);
            sex = __is.read(sex);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(userId);
            __os.write(username);
            __os.write(nickname);
            __os.write(sessionKey);
            __os.write(sex);
        }
    } // end of class SLoginReturn

    // class SMessage
    public static class SMessage extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SMessage();
            }
        }

        static {
            MessageBlock.regist("SMessage", new AutoRegist());
        }

        public short var1;
        public int var2;
        public long var3;
        public float var4;
        public double var5;
        public String var6;
        public Date var7;
        public publicdef.SeqInt intList;
        public publicdef.DictStringInt dictStrInt;

        public SMessage()
        {
            var1 = 0;
            var2 = 0;
            var3 = 0;
            var4 = 0;
            var5 = 0;
            var6 = "";
            var7 = new Date();
            intList = new publicdef.SeqInt();
            dictStrInt = new publicdef.DictStringInt();
        }

        @Override
        public void __read(Serializer __is)
        {
            var1 = __is.read(var1);
            var2 = __is.read(var2);
            var3 = __is.read(var3);
            var4 = __is.read(var4);
            var5 = __is.read(var5);
            var6 = __is.read(var6);
            var7 = __is.read(var7);
            intList.__read(__is);
            dictStrInt.__read(__is);
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(var1);
            __os.write(var2);
            __os.write(var3);
            __os.write(var4);
            __os.write(var5);
            __os.write(var6);
            __os.write(var7);
            intList.__write(__os);
            dictStrInt.__write(__os);
        }
    } // end of class SMessage

    // List SeqMessage
    public static class SeqMessage
    {
        private SMessage[] __array;

        public SeqMessage()
        {
            __array = null;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new SMessage[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                SMessage __val = new SMessage();
                __val.__read(__is);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __array[i].__write(__os);
            }
        }

    }

    // Dict DictMessage
    public static class DictMessage
    {
        private Map<Integer, SMessage> __map;

        public DictMessage()
        {
            __map = new HashMap<Integer, SMessage>();
        }

        public Map<Integer, SMessage> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                SMessage __val = new SMessage();
                __val.__read(__is);
                __map.put(__key, __val);
            }
        }

        public void __write(Serializer __os)
        {
            __os.write(__map.size());

            Set<Integer> __keySet = __map.keySet();
            Iterator<Integer> __it = __keySet.iterator();
            while (__it.hasNext())
            {
                Integer __key = __it.next();
                __os.write(__key.intValue());
                SMessage __val = __map.get(__key);
                __val.__write(__os);
            }
        }

    }

}


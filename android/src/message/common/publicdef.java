/*
* @filename publicdef.java
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

package message.common;


import java.util.Date;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;

import rmi.Serializer;
import rmi.MessageBlock;


public class publicdef
{
    // List SeqInt
    public static class SeqInt
    {
        private int[] __array;

        public SeqInt()
        {
            __array = null;
        }

        public int[] getArray()
        {
            return __array;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new int[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                int __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    }

    // List SeqLong
    public static class SeqLong
    {
        private long[] __array;

        public SeqLong()
        {
            __array = null;
        }

        public long[] getArray()
        {
            return __array;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new long[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                long __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    }

    // List SeqString
    public static class SeqString
    {
        private String[] __array;

        public SeqString()
        {
            __array = null;
        }

        public String[] getArray()
        {
            return __array;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new String[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                String __val = "";
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    }

    // List SeqFloat
    public static class SeqFloat
    {
        private float[] __array;

        public SeqFloat()
        {
            __array = null;
        }

        public float[] getArray()
        {
            return __array;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            __array = new float[__dataSize];
            for (int i = 0; i < __dataSize; ++i)
            {
                float __val = 0;
                __val = __is.read(__val);
                __array[i] = __val;
            }
        }

        public void __write(Serializer __os)
        {
            int __dataSize = (__array != null) ? __array.length : 0;
            __os.write(__dataSize);
            for (int i = 0; i < __dataSize; ++i)
            {
                __os.write(__array[i]);
            }
        }

    }

    // Dict DictIntInt
    public static class DictIntInt
    {
        private Map<Integer, Integer> __map;

        public DictIntInt()
        {
            __map = new HashMap<Integer, Integer>();
        }

        public Map<Integer, Integer> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                Integer __val = new Integer(__is.readInt());
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
                Integer __val = __map.get(__key);
                __os.write(__val.intValue());
            }
        }

    }

    // Dict DictIntString
    public static class DictIntString
    {
        private Map<Integer, String> __map;

        public DictIntString()
        {
            __map = new HashMap<Integer, String>();
        }

        public Map<Integer, String> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                Integer __key = new Integer(__is.readInt());
                String __val = "";
                __val = __is.read(__val);
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
                String __val = __map.get(__key);
                __os.write(__val);
            }
        }

    }

    // Dict DictStringInt
    public static class DictStringInt
    {
        private Map<String, Integer> __map;

        public DictStringInt()
        {
            __map = new HashMap<String, Integer>();
        }

        public Map<String, Integer> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                Integer __val = new Integer(__is.readInt());
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
                Integer __val = __map.get(__key);
                __os.write(__val.intValue());
            }
        }

    }

    // Dict DictStringString
    public static class DictStringString
    {
        private Map<String, String> __map;

        public DictStringString()
        {
            __map = new HashMap<String, String>();
        }

        public Map<String, String> getMap()
        {
            return __map;
        }

        public void __read(Serializer __is)
        {
            int __dataSize = __is.readInt();
            for (int i = 0; i < __dataSize; ++i)
            {
                String __key = __is.readString();
                String __val = "";
                __val = __is.read(__val);
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
                String __val = __map.get(__key);
                __os.write(__val);
            }
        }

    }

}


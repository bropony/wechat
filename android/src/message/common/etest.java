/*
* @filename etest.java
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
import rmi.RmiCore;
import rmi.MessageBlock;


public class etest
{
    // enum EHelloWorld
    public static class EHelloWorld
    {
        final public static int Hello = 0;
        final public static int World = 1;

    }

    // class SHelloEnum
    public static class SHelloEnum extends MessageBlock.MessageBase
    {
        public static class AutoRegist extends MessageBlock.AutoRegist
        {
            @Override
            public MessageBlock.MessageBase create()
            {
                return new SHelloEnum();
            }
        }

        static {
            MessageBlock.regist("SHelloEnum", new AutoRegist());
        }

        public int age;
        public String damn;
        public int greetType;

        public SHelloEnum()
        {
            age = 0;
            damn = "";
            greetType = EHelloWorld.Hello;
        }

        @Override
        public void __read(Serializer __is)
        {
            age = __is.read(age);
            damn = __is.read(damn);
            greetType = __is.readInt();
        }

        @Override
        public void __write(Serializer __os)
        {
            __os.write(age);
            __os.write(damn);
            __os.write(greetType);
        }
    } // end of class SHelloEnum

}


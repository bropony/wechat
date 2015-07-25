package message;

import rmi.MessageBlock;
import message.gate.gatemsg.SLoginReturn;
import message.gate.gatemsg.SSignup;
import message.gate.gatemsg.SMessage;
import message.gate.gatemsg.SLogin;
import message.gate.itest.ITestProxy;
import message.common.etest.SHelloEnum;

public class MessageRegister{
    public static void regist(){
        message.gate.gatemsg.SLoginReturn.__regist();
        message.gate.gatemsg.SSignup.__regist();
        message.gate.gatemsg.SMessage.__regist();
        message.gate.gatemsg.SLogin.__regist();
        message.gate.itest.ITestProxy.__regist();
        message.common.etest.SHelloEnum.__regist();
    }
}


package message;

import rmi.MessageBlock;
import message.gate.itest.ITestProxy;
import message.gate.gatemsg.SLogin;
import message.common.etest.SHelloEnum;
import message.gate.gatemsg.SLoginReturn;
import message.gate.gatemsg.SMessage;
import message.gate.gatemsg.SSignup;

public class MessageRegister{
    public static void regist(){
        message.gate.itest.ITestProxy.__regist();
        message.gate.gatemsg.SLogin.__regist();
        message.common.etest.SHelloEnum.__regist();
        message.gate.gatemsg.SLoginReturn.__regist();
        message.gate.gatemsg.SMessage.__regist();
        message.gate.gatemsg.SSignup.__regist();
    }
}


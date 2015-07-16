/*
* @filename itest.m
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "itest.h"

@implementation DictStrMessage
- (id) init
{
    self = [super init];
    if (!self) return self;

    _data = [[NSMutableDictionary alloc] init];
    return self;
}

- (void) __read: (GYSerializer *) __is
{
    GYInt dataSize = [__is readInt];
    for (GYInt i = 0; i < dataSize; ++i)
    {
        NSString * __key = @"";
        SMessage * __val = [[SMessage alloc] init];
        __key = [__is readString];
        [__val __read: __is];
        [_data setObject: __val forKey: __key];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[_data count];
    [__os writeInt: dataSize];
    for (id __key in [_data keyEnumerator])
    {
        [__os writeString: __key];

        id __val = [_data objectForKey: __key];
        [__val __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    DictStrMessage * __newDict = [[[self class] allocWithZone: zone] init];
    for (id __key in [_data keyEnumerator])
    {
        id __newKey = [__key copy];
        id __val = [_data objectForKey: __key];
        id __newVal = [__val copy];
        [[__newDict data] setObject: __newVal forKey: __newKey];
    }
    return __newDict;
}
@end


@implementation ITest_getIntList_response
- (id) init
{
    self = [super init];
    return self;
}

- (void) __onResponse: (GYSerializer *) __is
{
    SeqInt * intList = [[SeqInt alloc] init];
    [intList __read: __is];

    [self onResponseWithIntList: intList];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    [self onError: what code: code];
}

- (void) __onTimeout
{
    [self onTimeout];
}

- (void) onResponseWithIntList: (SeqInt *) intList
{
    // todo:
    // override this method in subclasses
}

- (void) onError: (NSString *) what code: (GYInt) code
{
    // todo:
    // override this method in subclasses
}

- (void) onTimeout
{
    // todo:
    // override this method in subclasses
}
@end


@implementation ITest_getDictIntString_response
- (id) init
{
    self = [super init];
    return self;
}

- (void) __onResponse: (GYSerializer *) __is
{
    DictIntString * intStrMap = [[DictIntString alloc] init];
    [intStrMap __read: __is];

    [self onResponseWithIntStrMap: intStrMap];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    [self onError: what code: code];
}

- (void) __onTimeout
{
    [self onTimeout];
}

- (void) onResponseWithIntStrMap: (DictIntString *) intStrMap
{
    // todo:
    // override this method in subclasses
}

- (void) onError: (NSString *) what code: (GYInt) code
{
    // todo:
    // override this method in subclasses
}

- (void) onTimeout
{
    // todo:
    // override this method in subclasses
}
@end


@implementation ITest_getFloatList_response
- (id) init
{
    self = [super init];
    return self;
}

- (void) __onResponse: (GYSerializer *) __is
{
    SeqFloat * floatList = [[SeqFloat alloc] init];
    [floatList __read: __is];

    GYInt dummy = 0;
    dummy = [__is readInt];

    [self onResponseWithFloatList: floatList andDummy: dummy];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    [self onError: what code: code];
}

- (void) __onTimeout
{
    [self onTimeout];
}

- (void) onResponseWithFloatList: (SeqFloat *) floatList andDummy: (GYInt) dummy
{
    // todo:
    // override this method in subclasses
}

- (void) onError: (NSString *) what code: (GYInt) code
{
    // todo:
    // override this method in subclasses
}

- (void) onTimeout
{
    // todo:
    // override this method in subclasses
}
@end


@implementation ITest_signup_response
- (id) init
{
    self = [super init];
    return self;
}

- (void) __onResponse: (GYSerializer *) __is
{
    SLoginReturn * loginReturn = [[SLoginReturn alloc] init];
    [loginReturn __read: __is];

    [self onResponseWithLoginReturn: loginReturn];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    [self onError: what code: code];
}

- (void) __onTimeout
{
    [self onTimeout];
}

- (void) onResponseWithLoginReturn: (SLoginReturn *) loginReturn
{
    // todo:
    // override this method in subclasses
}

- (void) onError: (NSString *) what code: (GYInt) code
{
    // todo:
    // override this method in subclasses
}

- (void) onTimeout
{
    // todo:
    // override this method in subclasses
}
@end


@implementation ITest_doNothing_response
- (id) init
{
    self = [super init];
    return self;
}

- (void) __onResponse: (GYSerializer *) __is
{
    [self onResponse];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    [self onError: what code: code];
}

- (void) __onTimeout
{
    [self onTimeout];
}

- (void) onResponse
{
    // todo:
    // override this method in subclasses
}

- (void) onError: (NSString *) what code: (GYInt) code
{
    // todo:
    // override this method in subclasses
}

- (void) onTimeout
{
    // todo:
    // override this method in subclasses
}
@end


@implementation ITestProxy
- (id) init
{
    self = [super initWithName: @"ITest"];
    return self;
}

- (void) getIntListWithResponse: (ITest_getIntList_response *) __response andSize: size
{
    GYSerializer * __os = [[GYSerializer alloc] init];
    [__os startToWrite];
    [__os writeByte: GYRmiDataCall];
    [__os writeString: [self name]];
    [__os writeString: @"getIntList"];

    GYInt __msgId = [GYRmiProxyBase getMsgId];
    [__os writeInt: __msgId];
    [__response setMsgId: __msgId];

    [__os writeInt: size];

    [self invoke: __os withCallback: __response];
}

- (void) getDictIntStringWithResponse: (ITest_getDictIntString_response *) __response andSize: size
{
    GYSerializer * __os = [[GYSerializer alloc] init];
    [__os startToWrite];
    [__os writeByte: GYRmiDataCall];
    [__os writeString: [self name]];
    [__os writeString: @"getDictIntString"];

    GYInt __msgId = [GYRmiProxyBase getMsgId];
    [__os writeInt: __msgId];
    [__response setMsgId: __msgId];

    [__os writeInt: size];

    [self invoke: __os withCallback: __response];
}

- (void) getFloatListWithResponse: (ITest_getFloatList_response *) __response andSize: size
{
    GYSerializer * __os = [[GYSerializer alloc] init];
    [__os startToWrite];
    [__os writeByte: GYRmiDataCall];
    [__os writeString: [self name]];
    [__os writeString: @"getFloatList"];

    GYInt __msgId = [GYRmiProxyBase getMsgId];
    [__os writeInt: __msgId];
    [__response setMsgId: __msgId];

    [__os writeInt: size];

    [self invoke: __os withCallback: __response];
}

- (void) signupWithResponse: (ITest_signup_response *) __response andSignup: signup
{
    GYSerializer * __os = [[GYSerializer alloc] init];
    [__os startToWrite];
    [__os writeByte: GYRmiDataCall];
    [__os writeString: [self name]];
    [__os writeString: @"signup"];

    GYInt __msgId = [GYRmiProxyBase getMsgId];
    [__os writeInt: __msgId];
    [__response setMsgId: __msgId];

    [signup __write: __os];

    [self invoke: __os withCallback: __response];
}

- (void) doNothingWithResponse: (ITest_doNothing_response *) __response
{
    GYSerializer * __os = [[GYSerializer alloc] init];
    [__os startToWrite];
    [__os writeByte: GYRmiDataCall];
    [__os writeString: [self name]];
    [__os writeString: @"doNothing"];

    GYInt __msgId = [GYRmiProxyBase getMsgId];
    [__os writeInt: __msgId];
    [__response setMsgId: __msgId];

    [self invoke: __os withCallback: __response];
}

@end



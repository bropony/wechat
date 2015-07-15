/*
* @filename gatemsg.m
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "message/gate/gatemsg.h"

@implementation SeqSeqInt
- (id) init
{
    self = [super init];
    if (!self) return self;

    _data = [[NSMutableArray alloc] init];
    return self;
}

- (void) __read: (GYSerializer *) __is
{
    GYInt dataSize = [__is readInt];
    for (GYInt i = 0; i < dataSize; ++i)
    {
        SeqInt * __tmpObj = [[SeqInt alloc] init];
        [__tmpObj __read: __is];
        [_data addObject: __tmpObj];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [id __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newList = [[[self class] allocWithZone: zone] init];
    for (id __obj in _data)
    {
        id __newObj = [__obj copy];
        [__newList.data addObject: __newObj];
    }
    return __newList;
}
@end


@implementation SeqDictIntInt
- (id) init
{
    self = [super init];
    if (!self) return self;

    _data = [[NSMutableArray alloc] init];
    return self;
}

- (void) __read: (GYSerializer *) __is
{
    GYInt dataSize = [__is readInt];
    for (GYInt i = 0; i < dataSize; ++i)
    {
        DictIntInt * __tmpObj = [[DictIntInt alloc] init];
        [__tmpObj __read: __is];
        [_data addObject: __tmpObj];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [id __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newList = [[[self class] allocWithZone: zone] init];
    for (id __obj in _data)
    {
        id __newObj = [__obj copy];
        [__newList.data addObject: __newObj];
    }
    return __newList;
}
@end


@implementation DictDictStringInt
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
        GYInt __key = 0;
        DictStringInt * __val = [[DictStringInt alloc] init];
        __key = [__is readInt];
        [__val __read: __is];
        [_data setObject: __val forKey: [NSNumber numberWithInt: __key]];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[_data count];
    [__os writeInt: dataSize];
    for (id __key in [_data keyEnumerator])
    {
        [__os writeInt: [__key intValue]];

        id __val = [_data objectForKey: __key];
        [__val __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newDict = [[[self class] allocWithZone: zone] init];
    for (id __key in [_data keyEnumerator])
    {
        id __newKey = [__key copy];
        id __val = [_data objectForKey: __key];
        id __newVal = [__val copy];
        [__newDict.data setObject: __newVal forKey: __newKey];
    }
    return __newDict;
}
@end


@implementation SSignup

@synthesize NSString * username;
@synthesize NSString * nickname;
@synthesize NSString * password;
@synthesize GYInt sex;

- (id) init
{
    self = [super init];
    if (!self) return self;

    username = @"";
    nickname = @"";
    password = @"";
    sex = 0;

    return self;
}

- (void) __read: (GYSerializer *) __is
{
    username = [__is readString];
    nickname = [__is readString];
    password = [__is readString];
    sex = [__is readInt];
}

- (void) __write: (GYSerializer *) __os
{
    [__os writeString: username];
    [__os writeString: nickname];
    [__os writeString: password];
    [__os writeInt: sex];
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newObj = [[[self class] allocWithZone: zone] init];

    __newObj.username = [self.username copy];
    __newObj.nickname = [self.nickname copy];
    __newObj.password = [self.password copy];
    __newObj.sex = self.sex;

    return __newObj;
}
@end


@implementation SLogin

@synthesize NSString * username;
@synthesize NSString * password;

- (id) init
{
    self = [super init];
    if (!self) return self;

    username = @"";
    password = @"";

    return self;
}

- (void) __read: (GYSerializer *) __is
{
    username = [__is readString];
    password = [__is readString];
}

- (void) __write: (GYSerializer *) __os
{
    [__os writeString: username];
    [__os writeString: password];
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newObj = [[[self class] allocWithZone: zone] init];

    __newObj.username = [self.username copy];
    __newObj.password = [self.password copy];

    return __newObj;
}
@end


@implementation SLoginReturn

@synthesize GYInt userId;
@synthesize NSString * username;
@synthesize NSString * nickname;
@synthesize NSString * sessionKey;
@synthesize GYInt sex;

- (id) init
{
    self = [super init];
    if (!self) return self;

    userId = 0;
    username = @"";
    nickname = @"";
    sessionKey = @"";
    sex = 0;

    return self;
}

- (void) __read: (GYSerializer *) __is
{
    userId = [__is readInt];
    username = [__is readString];
    nickname = [__is readString];
    sessionKey = [__is readString];
    sex = [__is readInt];
}

- (void) __write: (GYSerializer *) __os
{
    [__os writeInt: userId];
    [__os writeString: username];
    [__os writeString: nickname];
    [__os writeString: sessionKey];
    [__os writeInt: sex];
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newObj = [[[self class] allocWithZone: zone] init];

    __newObj.userId = self.userId;
    __newObj.username = [self.username copy];
    __newObj.nickname = [self.nickname copy];
    __newObj.sessionKey = [self.sessionKey copy];
    __newObj.sex = self.sex;

    return __newObj;
}
@end


@implementation SMessage

@synthesize GYShort var1;
@synthesize GYInt var2;
@synthesize GYLong var3;
@synthesize GYFloat var4;
@synthesize GYDouble var5;
@synthesize NSString * var6;
@synthesize NSDate * var7;
@synthesize SeqInt * intList;
@synthesize DictStringInt * dictStrInt;

- (id) init
{
    self = [super init];
    if (!self) return self;

    var1 = 0;
    var2 = 0;
    var3 = 0;
    var4 = 0.0;
    var5 = 0.0;
    var6 = @"";
    var7 = [NSDate date];
    intList = [[SeqInt alloc] init];
    dictStrInt = [[DictStringInt alloc] init];

    return self;
}

- (void) __read: (GYSerializer *) __is
{
    var1 = [__is readShort];
    var2 = [__is readInt];
    var3 = [__is readLong];
    var4 = [__is readFloat];
    var5 = [__is readDouble];
    var6 = [__is readString];
    var7 = [__is readDate];
    [intList __read: __is];
    [dictStrInt __read: __is];
}

- (void) __write: (GYSerializer *) __os
{
    [__os writeShort: var1];
    [__os writeInt: var2];
    [__os writeLong: var3];
    [__os writeFloat: var4];
    [__os writeDouble: var5];
    [__os writeString: var6];
    [__os writeDate: var7];
    [intList __write: __os];
    [dictStrInt __write: __os];
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newObj = [[[self class] allocWithZone: zone] init];

    __newObj.var1 = self.var1;
    __newObj.var2 = self.var2;
    __newObj.var3 = self.var3;
    __newObj.var4 = self.var4;
    __newObj.var5 = self.var5;
    __newObj.var6 = [self.var6 copy];
    __newObj.var7 = [self.var7 copy];
    __newObj.intList = [self.intList copy];
    __newObj.dictStrInt = [self.dictStrInt copy];

    return __newObj;
}
@end


@implementation SeqMessage
- (id) init
{
    self = [super init];
    if (!self) return self;

    _data = [[NSMutableArray alloc] init];
    return self;
}

- (void) __read: (GYSerializer *) __is
{
    GYInt dataSize = [__is readInt];
    for (GYInt i = 0; i < dataSize; ++i)
    {
        SMessage * __tmpObj = [[SMessage alloc] init];
        [__tmpObj __read: __is];
        [_data addObject: __tmpObj];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [id __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newList = [[[self class] allocWithZone: zone] init];
    for (id __obj in _data)
    {
        id __newObj = [__obj copy];
        [__newList.data addObject: __newObj];
    }
    return __newList;
}
@end


@implementation DictMessage
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
        GYInt __key = 0;
        SMessage * __val = [[SMessage alloc] init];
        __key = [__is readInt];
        [__val __read: __is];
        [_data setObject: __val forKey: [NSNumber numberWithInt: __key]];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[_data count];
    [__os writeInt: dataSize];
    for (id __key in [_data keyEnumerator])
    {
        [__os writeInt: [__key intValue]];

        id __val = [_data objectForKey: __key];
        [__val __write: __os];
    }
}

- (id) copyWithZone: (NSZone *) zone
{
    id __newDict = [[[self class] allocWithZone: zone] init];
    for (id __key in [_data keyEnumerator])
    {
        id __newKey = [__key copy];
        id __val = [_data objectForKey: __key];
        id __newVal = [__val copy];
        [__newDict.data setObject: __newVal forKey: __newKey];
    }
    return __newDict;
}
@end



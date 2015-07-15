/*
* @filename publicdef.m
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "message/common/publicdef.h"

@implementation SeqInt
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
        GYInt __tmpObj = 0;
        __tmpObj = [__is readInt];
        [_data addObject: [NSNumber numberWithInt: __tmpObj]];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [__os writeInt: [id intValue]];
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


@implementation SeqLong
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
        GYLong __tmpObj = 0;
        __tmpObj = [__is readLong];
        [_data addObject: [NSNumber numberWithLong: __tmpObj]];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [__os writeLong: [id longValue]];
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


@implementation SeqString
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
        NSString * __tmpObj = @"";
        __tmpObj = [__is readString];
        [_data addObject: __tmpObj];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [__os writeString: id];
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


@implementation SeqFloat
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
        GYFloat __tmpObj = 0.0;
        __tmpObj = [__is readFloat];
        [_data addObject: [NSNumber numberWithFloat: __tmpObj]];
    }
}

- (void) __write: (GYSerializer *) __os
{
    GYInt dataSize = (GYInt)[data count];
    for (id obj in _data)
    {
        [__os writeFloat: [id floatValue]];
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


@implementation DictIntInt
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
        GYInt __val = 0;
        __key = [__is readInt];
        __val = [__is readInt];
        [_data setObject: [NSNumber numberWithInt: __val] forKey: [NSNumber numberWithInt: __key]];
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
        [__os writeInt: [__val intValue]];
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


@implementation DictIntString
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
        NSString * __val = @"";
        __key = [__is readInt];
        __val = [__is readString];
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
        [__os writeString: __val];
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


@implementation DictStringInt
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
        GYInt __val = 0;
        __key = [__is readString];
        __val = [__is readInt];
        [_data setObject: [NSNumber numberWithInt: __val] forKey: __key];
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
        [__os writeInt: [__val intValue]];
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


@implementation DictStringString
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
        NSString * __val = @"";
        __key = [__is readString];
        __val = [__is readString];
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
        [__os writeString: __val];
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



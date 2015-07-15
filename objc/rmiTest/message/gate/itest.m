/*
* @filename itest.m
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "message/gate/itest.h"

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



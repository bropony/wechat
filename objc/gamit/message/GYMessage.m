//
//  GYMessage.m
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import "GYMessage.h"

static NSMutableSet * gMsgClassSet = nil;

@implementation GYMessageBlock
+ (id<GYMessageBaseProtocol>) createWithName: (NSString *) className
{
    id<GYMessageBaseProtocol> msg = [[NSClassFromString(className) alloc] init];
    
    return msg;
}

+ (void) registMessage: (NSString *) className
{
    if (!gMsgClassSet)
    {
        gMsgClassSet = [[NSMutableSet alloc] init];
    }
    
    [gMsgClassSet addObject: className];
}

- (id) initWithData: (GYSerializer *) __is
{
    self = [super init];
    if (!self)
    {
        return self;
    }
    
    _command = [__is readInt];
    
    GYInt idSize = [__is readInt];
    for (int i = 0; i < idSize; ++i)
    {
        [__is readInt];
    }
    
    NSString * name = [__is readString];
    _messageBase = [GYMessageBlock createWithName: name];
    [_messageBase __read: __is];
    
    return self;
}

@end
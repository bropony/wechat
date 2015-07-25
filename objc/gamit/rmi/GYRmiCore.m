//
//  GYRmiCore.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYRmiCore.h"
#import "GYSerializingError.h"

//GYRmiRepsonseBase
@implementation GYRmiResponseBase
{
    NSDate * _createDt;
}

- (id) init
{
    self = [super init];
    
    if (self)
    {
        _msgId = 0;
        _createDt = [NSDate date];
    }
    
    return  self;
}

- (BOOL) isExpiredTil:(NSDate *)endDt withinInterval:(GYLong)interval
{
    GYLong passedSecs = [endDt timeIntervalSince1970] - [_createDt timeIntervalSince1970];
    
    if (interval <= passedSecs)
    {
        return YES;
    }
    
    return NO;
}

- (void) __onResponse:(GYSerializer *)__is
{
    NSString * what = @"GYRmiResponseBase.__onResponse must be overriden";
    @throw [[GYSerializingError alloc] initWhat: what andCode: 0];
}

- (void) __onError: (NSString *) what code: (GYInt) code
{
    NSString * __what = @"GYRmiResponseBase.__onError must be overriden";
    @throw [[GYSerializingError alloc] initWhat: __what andCode: 0];
}

- (void) __onTimeout
{
    NSString * what = @"GYRmiResponseBase.__onTimeout must be overriden";
    @throw [[GYSerializingError alloc] initWhat: what andCode: 0];
}

@end

static int gMsgIdBase = 0;
//GYRmiProxyBase
@implementation GYRmiProxyBase
{
    NSString * _name;
    __weak id<GYRmiClientProtocal> _rmiClient;
}

+ (int) getMsgId
{
    gMsgIdBase += 1;
    return gMsgIdBase;
}

- (id) init
{
    self = [super init];
    
    if (self)
    {
        return [self initWithName:@"" rmiClient: nil];
    }
    
    return self;
}

- (id) initWithName:(NSString *)name
{
    self = [super init];
    
    if (self)
    {
        return [self initWithName: name rmiClient: nil];
    }
    
    return self;
}

- (id) initWithName: (NSString *) name rmiClient: (id<GYRmiClientProtocal>) rmiClient;
{
    self = [super init];
    
    if (self)
    {
        _name = name;
        _rmiClient = rmiClient;
    }
    
    return self;
}

- (void) setRmiClient:(id<GYRmiClientProtocal>)rmiClient
{
    _rmiClient = rmiClient;
}

- (NSString *) name
{
    return _name;
}

- (void) invoke:(GYSerializer *)__os withCallback:(GYRmiResponseBase *)callback
{
    [_rmiClient onCall: __os withCallback: callback];
}
@end
//
//  GYProxyManager.m
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import "GYProxyManager.h"

static GYProxyManager * gProxyManagerInstance = nil;

@interface GYProxyManager()
- (id) init;
@end

@implementation GYProxyManager
{
    NSMutableDictionary * _proxyDict;
}

+ (GYProxyManager *) instance
{
    if (!gProxyManagerInstance)
    {
        gProxyManagerInstance = [[GYProxyManager alloc] init];
    }
    
    return gProxyManagerInstance;
}

- (id) init
{
    self = [super init];
    if (self)
    {
        _proxyDict = [[NSMutableDictionary alloc] init];
    }
    
    return self;
}

- (void) addProxy: (GYRmiProxyBase *) proxy
{
    [_proxyDict setValue: proxy forKey: [proxy name]];
}

- (GYRmiProxyBase *) getProxy: (NSString *) name
{
    return [_proxyDict objectForKey: name];
}

@end

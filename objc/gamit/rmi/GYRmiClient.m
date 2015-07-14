//
//  GYRmiClient.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYRmiClient.h"
#import "GYWSConnector.h"

@implementation GYRmiClient
{
    GYWSConnector * _connector;
    BOOL _isOpen;
    
    NSMutableDictionary * _callbackDict;
    NSMutableDictionary * _proxyDict;
    
    id<GYRmiConnectionOpenCallbackProtocol> _onOpenCallback;
}

- (id) initWithIp: (NSString *) ip andPort: (int) port
{
    self = [super init];
    
    if (NULL == self)
    {
        return self;
    }
    
    _connector = [[GYWSConnector alloc] initWithIp: ip andPort: port];
    _isOpen = NO;
    
    _callbackDict = [[NSMutableDictionary alloc] init];
    _proxyDict = [[NSMutableDictionary alloc] init];
    
    return self;
}

- (void) start
{
    [_connector start];
}

- (void) stop
{
    [_connector stop];
    
    [_callbackDict removeAllObjects];
    [_proxyDict removeAllObjects];
}

- (void) checkCallbackTimeout
{
    
}

- (void) onOpen
{
    
}

- (void) onCloseWithCode:(NSInteger) code reason:(NSString *) reason
{
    
}

- (void) onError: (NSError *)error
{
    
}

- (void) onMessage: (id) data
{
    
}

- (void) send: (GYSerializer *) __os
{
    
}

- (void) sendWithData: (NSData *) data
{
    
}

- (void) sendWithString: (NSString *) str
{
    
}

- (void) connect
{
    
}

- (void) disconnect
{
    
}

- (void) onCall: (GYSerializer *) __os withCallback: (GYRmiResponseBase *) callbak
{
    
}

- (void) addResponse: (GYRmiResponseBase *) response
{
    
}

- (void) setConnectionOpenCallback: (id<GYRmiConnectionOpenCallbackProtocol>) callback
{
    
}
@end

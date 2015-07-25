//
//  GYRmiClient.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYRmiClient.h"
#import "GYWSConnector.h"
#import "GYLogger.h"
#import "GYSerializingError.h"
#import "GYMessageManager.h"
#import "GYProxyManager.h"


//impl...
@implementation GYRmiClient
{
    GYWSConnector * _connector;
    BOOL _isNetworkOk;
    BOOL _isConnecting;
    NSDate * _firstConnectTryDt;
    GYInt _timeout;
    
    NSMutableDictionary * _callbackDict;
    NSMutableDictionary * _proxyDict;
    NSMutableArray * _cachedRequestArray;
    
    id<GYRmiConnectionOpenCallbackProtocol> _onOpenCallback;
}

- (id) initWithIp: (NSString *) ip andPort: (int) port
{
    self = [super init];
    
    if (!self)
    {
        return self;
    }
    
    _connector = [[GYWSConnector alloc] initWithIp: ip andPort: port];
    [_connector setRmiClient: self];
    
    _isNetworkOk = NO;
    _isConnecting = NO;
    _firstConnectTryDt = nil;
    _timeout = 20; // default 20 secs
    
    _callbackDict = [[NSMutableDictionary alloc] init];
    _proxyDict = [[NSMutableDictionary alloc] init];
    _cachedRequestArray = [[NSMutableArray alloc] init];
    
    _onOpenCallback = nil;
    
    return self;
}

- (void) setCallbackTimeout:(GYInt)timeoutSecs
{
    _timeout = timeoutSecs;
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
    [_cachedRequestArray removeAllObjects];
}

- (void) fireOut
{
    [self digestUnsentRequest];
    [self checkCallbacksTimout];
}

- (void) onOpen
{
    [GYLogger log: @"Network connection established"];
    
    _isNetworkOk = YES;
    _isConnecting = NO;
    _firstConnectTryDt = nil;
    
    if (_onOpenCallback)
    {
        [_onOpenCallback onOpen];
    }
}

- (void) onCloseWithCode:(NSInteger) code reason:(NSString *) reason
{
    [GYLogger log: @"Network connection closed"];
    
    _isNetworkOk = NO;
    _isConnecting = NO;
    _firstConnectTryDt = nil;
}

- (void) onError: (NSError *)error
{
    [GYLogger log: [NSString stringWithFormat: @"Network error: %@", error]];
    
    _isConnecting = NO;
    _isNetworkOk = NO;
}

- (void) onMessage: (id) data
{
    if ([data isKindOfClass: [NSData class]])
    {
        GYSerializer * __is = [[GYSerializer alloc] initWithData: data];
        [__is simpleDecrypt];
        [__is startToRead];
        
        GYByte rmiType = [__is readByte];
        switch (rmiType) {
            case GYRmiDataResponse:
                {
                    [self _onRmiResponse: __is];
                }
                break;
            case GYRmiDataException:
                {
                    [self _onRmiError: __is];
                }
                break;
            case GYRmiDataMessageBlock:
                {
                    [self _onRmiMessage: __is];
                }
                break;
            default:
                {
                    @throw [[GYSerializingError alloc] initWhat: @"Unknow GYRmiDataType" andCode: 0];
                }
                break;
        }
    }
    else if ([data isKindOfClass: [NSString class]])
    {
        //todo
        [GYLogger log: [NSString stringWithFormat: @"GYRmiClient: %@", @"plain text received..."]];
    }
    else
    {
        [GYLogger log: [NSString stringWithFormat: @"GYRmiClient: %@", @"Unregconised data type..."]];
    }
}

- (void) _onRmiResponse: (GYSerializer *) __is
{
    GYInt msgId = [__is readInt];
    NSNumber * key = [[NSNumber alloc] initWithInt: msgId];
    
    id response = [_callbackDict objectForKey: key];
    
    if (response)
    {
        [response __onResponse: __is];
        
        [_callbackDict removeObjectForKey: key];
    }
}

- (void) _onRmiMessage: (GYSerializer *) __is
{
    [[GYMessageManager instance] onMessage: __is];
}

- (void) _onRmiError: (GYSerializer *) __is
{
    GYInt msgId = [__is readInt];
    NSNumber * key = [[NSNumber alloc] initWithInt: msgId];
    
    NSString * what = [__is readString];
    GYInt code = [__is readInt];
    
    id response = [_callbackDict objectForKey: key];
    
    if (response)
    {
        [response __onError: what code: code];
        
        [_callbackDict removeObjectForKey: key];
    }
}

- (void) send: (GYSerializer *) __os
{
    [__os simpleEncrypt];
    
    [self sendWithData: [__os getBuffer]];
}

- (void) sendWithData: (NSData *) data
{
    [self sendOut: data];
}

- (void) sendWithString: (NSString *) str
{
    [self sendOut: str];
}

- (void) sendOut: (id) data
{
    if (_isNetworkOk)
    {
        [_connector send: data];
    }
    else
    {
        [_cachedRequestArray addObject: data];
    }
}

- (void) connect
{
    if (_isConnecting)
    {
        return;
    }
    
    /*if (_firstConnectTryDt)
    {
        NSDate * now = [NSDate date];
        if ([now timeIntervalSinceDate: _firstConnectTryDt] > 300)
        {
            // give up connection request after 5m...
            return;
        }
    }
    else
    {
        _firstConnectTryDt = [NSDate date];
    }*/
    
    NSLog(@"RmiClient Connecting To Server....");
    
    _isConnecting = YES;
    
    [_connector _connect];
}

- (void) disconnect
{
    [GYLogger log: @"Manually distconnecting network"];
    
    _isConnecting = NO;
    _isNetworkOk = NO;
    _firstConnectTryDt = nil;
    
    [_connector close];
    [_cachedRequestArray removeAllObjects];
}

- (void) onCall: (GYSerializer *) __os withCallback: (GYRmiResponseBase *) callbak
{
    [self send: __os];
    
    [self addResponse: callbak];
}

- (void) addResponse: (GYRmiResponseBase *) response
{
    if (response)
    {
        NSNumber * key = [NSNumber numberWithInt: [response msgId]];
        [_callbackDict setObject: response forKey: key];
    }
}

- (void) setConnectionOpenCallback: (id<GYRmiConnectionOpenCallbackProtocol>) callback
{
    _onOpenCallback = callback;
}

- (void) addProxy: (GYRmiProxyBase *) proxy
{
    [[GYProxyManager instance] addProxy: proxy];
    [proxy setRmiClient: self];
}

- (void) digestUnsentRequest
{
    if (0 == [_cachedRequestArray count])
    {
        return;
    }
    
    if (!_isNetworkOk)
    {
        [self connect];
        return;
    }
    
    for (id obj in _cachedRequestArray)
    {
        [self sendOut: obj];
    }
    
    [_cachedRequestArray removeAllObjects];
}

- (void) checkCallbacksTimout
{
    NSMutableArray * keyToRemove = [[NSMutableArray alloc] init];
    NSEnumerator * keyEnumerator = [_callbackDict keyEnumerator];
    NSDate * now = [NSDate date];
    
    for (id key in keyEnumerator)
    {
        id obj = [_callbackDict objectForKey: key];
        if ([obj isExpiredTil: now withinInterval: _timeout])
        {
            [keyToRemove addObject: key];
            [obj __onTimeout];
        }
    }
    
    for (id key in keyToRemove)
    {
        [_callbackDict removeObjectForKey: key];
    }
}
@end

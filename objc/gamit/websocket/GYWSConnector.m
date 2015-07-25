//
//  GYWSConnector.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYWSConnector.h"

@implementation GYWSConnector
{
    id<GYRmiClientProtocal> _rmiClient;
    SRWebSocket * _ws;
    NSURL * _wsUrl;
    NSString * _ip;
    int _port;
    
    BOOL _running;
}

- (id) initWithIp:(NSString *)ip andPort:(int)port
{
    self = [super init];
    
    if (self)
    {
        _ws = nil;
        _ip = ip;
        _port = port;
        
        NSString * strUrl = [NSString stringWithFormat:@"ws://%@:%i", _ip, _port];
        _wsUrl = [NSURL URLWithString: strUrl];
        
        _running = NO;
    }
    
    return self;
}

- (void) setRmiClient:(id<GYRmiClientProtocal>)rmiClient
{
    _rmiClient = rmiClient;
}

- (void) start
{
    //[self _connect];
    
    //_running = YES;
}

- (void) stop
{
    _running = NO;
    [self close];
}

- (void) send: (id) data
{
    [_ws send: data];
}

- (void) close
{
    if (nil != _ws)
    {
        [_ws close];
        _ws.delegate = nil;
        _ws = nil;
    }
}

- (void) _connect
{
    if (_ws != nil)
    {
        [self close];
    }
    
    NSLog( @"SRConnector connecting to Server...");
    
    _ws = [[SRWebSocket alloc] initWithURLRequest: [NSURLRequest requestWithURL: _wsUrl]];
    _ws.delegate = self;
    
    [_ws open];
}

- (void) _reconnect
{
    [self _connect];
}

- (void) webSocket:(SRWebSocket *)webSocket didReceiveMessage:(id)message
{
    [_rmiClient onMessage: message];
}

- (void)webSocketDidOpen:(SRWebSocket *)webSocket
{
    [_rmiClient onOpen];
    _running = YES;
}

- (void)webSocket:(SRWebSocket *)webSocket didFailWithError:(NSError *)error
{
    [_rmiClient onError: error];
    [self stop];
}

- (void)webSocket:(SRWebSocket *)webSocket didCloseWithCode:(NSInteger)code reason:(NSString *)reason wasClean:(BOOL)wasClean
{
    [_rmiClient onCloseWithCode: code reason: reason];
    [self stop];
}

- (void)webSocket:(SRWebSocket *)webSocket didReceivePong:(NSData *)pongPayload
{
    
}
@end

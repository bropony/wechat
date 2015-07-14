//
//  GYWSConnector.h
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import <Foundation/Foundation.h>
#import "SRWebSocket.h"
#import "GYRmiCore.h"

@interface GYWSConnector : NSObject <SRWebSocketDelegate>

- (id) initWithIp: (NSString *) ip andPort: (int) port;
- (void) setRmiClient: (id<GYRmiClientProtocal>) rmiClient;

- (void) start;
- (void) stop;

- (void) send: (id) data;
- (void) close;

#pragma mark - connect
- (void) _connect;
- (void) _reconnect;

#pragma mark - SRWebSocketDelegate
- (void) webSocket:(SRWebSocket *)webSocket didReceiveMessage:(id)message;
- (void)webSocketDidOpen:(SRWebSocket *)webSocket;
- (void)webSocket:(SRWebSocket *)webSocket didFailWithError:(NSError *)error;
- (void)webSocket:(SRWebSocket *)webSocket didCloseWithCode:(NSInteger)code reason:(NSString *)reason wasClean:(BOOL)wasClean;
- (void)webSocket:(SRWebSocket *)webSocket didReceivePong:(NSData *)pongPayload;
@end

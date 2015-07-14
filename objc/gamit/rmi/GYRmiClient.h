//
//  GYRmiClient.h
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import <Foundation/Foundation.h>
#import "GYRmiCore.h"

@interface GYRmiClient : NSObject <GYRMiClientProtocol>
- (id) initWithIp: (NSString *) ip andPort: (int) port;
- (void) start;
- (void) stop;
- (void) checkCallbackTimeout; // run in a every event loop;

- (void) onOpen;
- (void) onCloseWithCode:(NSInteger) code reason:(NSString *) reason;
- (void) onError: (NSError *)error;
- (void) onMessage: (id) data;
- (void) send: (GYSerializer *) __os;
- (void) sendWithData: (NSData *) data;
- (void) sendWithString: (NSString *) str;

- (void) connect;
- (void) disconnect;

- (void) onCall: (GYSerializer *) __os withCallback: (GYRmiResponseBase *) callbak;

- (void) addResponse: (GYRmiResponseBase *) response;
- (void) setConnectionOpenCallback: (id<GYRmiConnectionOpenCallbackProtocol>) callback;
@end

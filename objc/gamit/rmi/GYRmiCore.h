//
//  GYRmiCore.h
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import <Foundation/Foundation.h>
#import "GYSerializer.h"

@class GYRmiResponseBase;

@protocol GYRmiConnectionOpenCallbackProtocol
- (void) onOpen;
@end

@protocol GYRmiClientProtocal
- (void) onOpen;
- (void) onCloseWithCode:(NSInteger) code reason:(NSString *) reason;
- (void) onError: (NSError *)error;
- (void) onMessage: (id) data;
- (void) send: (GYSerializer *) __os;
- (void) sendWithData: (NSData *) data;
- (void) sendWithString: (NSString *) str;
- (void) start;
- (void) stop;

- (void) onCall: (GYSerializer *) __os withCallback: (GYRmiResponseBase *) callbak;

- (void) addResponse: (GYRmiResponseBase *) response;
- (void) setConnectionOpenCallback: (id<GYRmiConnectionOpenCallbackProtocol>) callback;
@end

@interface GYRmiResponseBase : NSObject
@property int msgId;

- (id) init;
- (BOOL) isExpiredTil: (NSDate *) endDt withinInterval: (GYLong) interval;

- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) error code: (int) code;
- (void) __onTimeout;
@end

@interface GYRmiProxyBase : NSObject
+ (int) getMsgId;

- (id) init;
- (id) initWithName: (NSString *) name;
- (id) initWithName: (NSString *) name rmiClient: (id<GYRmiClientProtocal>) rmiClient;

- (void) setRmiClient:(id<GYRmiClientProtocal>) rmiClient;
- (NSString *) name;
- (void) invoke: (GYSerializer *) __os withCallback: (GYRmiResponseBase *) callback;
@end

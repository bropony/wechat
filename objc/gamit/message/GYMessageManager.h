//
//  GYMessageManager.h
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import <Foundation/Foundation.h>
#import "GYMessage.h"

@interface GYMessageManager : NSObject
+ (GYMessageManager *) instance;

- (id) init;
- (void) registCommand: (int) command withHandler: (id<GYMessageBaseProtocol>) handler;
- (void) onMessage: (GYSerializer *) __is;
@end

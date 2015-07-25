//
//  GYMessage.h
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import <Foundation/Foundation.h>
#import "GYSerializer.h"

@protocol GYMessageBaseProtocol <NSCopying>
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
@end


@interface GYMessageBlock: NSObject
@property int command;
@property (copy, nonatomic) id<GYMessageBaseProtocol> messageBase;

+ (id<GYMessageBaseProtocol>) createWithName: (NSString *) className;
+ (void) registMessage: (NSString *) className;

- (id) initWithData: (GYSerializer *) __is;
@end


@protocol GYMessageCommandHandlerProtocal <NSObject>
- (void) onMessage: (GYMessageBlock *) messageBlock;
@end

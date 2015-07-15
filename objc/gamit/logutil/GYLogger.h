//
//  GYLogger.h
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import <Foundation/Foundation.h>

@interface GYLogger : NSObject
/*
 * For simple usage.
 * Please modify it into a more sophisticated logger in production.
 */
+ (void) log: (NSString *) info, ...;
@end

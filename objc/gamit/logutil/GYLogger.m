//
//  GYLogger.m
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import "GYLogger.h"

@implementation GYLogger
+ (void) log: (NSString *) info;
{
    NSLog(@"%@", info);
}
@end

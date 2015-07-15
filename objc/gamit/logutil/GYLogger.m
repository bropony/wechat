//
//  GYLogger.m
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import "GYLogger.h"

@implementation GYLogger
+ (void) log: (NSString *) info, ...;
{
    NSMutableString * str = [[NSMutableString alloc] init];
    
    if (info)
    {
        id arg;
        va_list argList;
        
        va_start(argList, info);
        while ((arg = va_arg(argList, id))) {
            [str appendFormat: @"%@\t", arg];
        }
        va_end(argList);
    }
    
    NSLog(@"%@", str);
}
@end

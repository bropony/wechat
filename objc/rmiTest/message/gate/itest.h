/*
* @filename itest.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "gamit/gamit.h"
#import "message/common/publicdef.h"
#import "message/gate/gatemsg.h"

// DictStrMessage
@interface DictStrMessage: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end



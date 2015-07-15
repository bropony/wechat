/*
* @filename publicdef.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "gamit/gamit.h"

// SeqInt
@interface SeqInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// SeqLong
@interface SeqLong: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// SeqString
@interface SeqString: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// SeqFloat
@interface SeqFloat: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictIntInt
@interface DictIntInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictIntString
@interface DictIntString: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictStringInt
@interface DictStringInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictStringString
@interface DictStringString: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end



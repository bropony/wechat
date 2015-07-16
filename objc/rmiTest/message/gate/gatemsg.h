/*
* @filename gatemsg.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "gamit.h"
#import "publicdef.h"

// SeqSeqInt
@interface SeqSeqInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// SeqDictIntInt
@interface SeqDictIntInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictDictStringInt
@interface DictDictStringInt: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// class SSignup
@interface SSignup: NSObject <GYMessageBaseProtocol>

@property (copy, nonatomic) NSString * username;
@property (copy, nonatomic) NSString * nickname;
@property (copy, nonatomic) NSString * password;
@property GYInt sex;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// class SLogin
@interface SLogin: NSObject <GYMessageBaseProtocol>

@property (copy, nonatomic) NSString * username;
@property (copy, nonatomic) NSString * password;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// class SLoginReturn
@interface SLoginReturn: NSObject <GYMessageBaseProtocol>

@property GYInt userId;
@property (copy, nonatomic) NSString * username;
@property (copy, nonatomic) NSString * nickname;
@property (copy, nonatomic) NSString * sessionKey;
@property GYInt sex;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// class SMessage
@interface SMessage: NSObject <GYMessageBaseProtocol>

@property GYShort var1;
@property GYInt var2;
@property GYLong var3;
@property GYFloat var4;
@property GYDouble var5;
@property (copy, nonatomic) NSString * var6;
@property (copy, nonatomic) NSDate * var7;
@property (copy, nonatomic) SeqInt * intList;
@property (copy, nonatomic) DictStringInt * dictStrInt;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// SeqMessage
@interface SeqMessage: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableArray * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// DictMessage
@interface DictMessage: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end



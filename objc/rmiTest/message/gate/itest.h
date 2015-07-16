/*
* @filename itest.h
*
* @author ahda86@gmail.com
*
* @brief This files is Auto-Generated. Please DON'T modify it EVEN if
*        you know what you are doing.
*/

#import "gamit.h"
#import "publicdef.h"
#import "gatemsg.h"

// DictStrMessage
@interface DictStrMessage: NSObject <GYMessageBaseProtocol>
@property (copy, nonatomic) NSMutableDictionary * data;

- (id) init;
- (void) __read: (GYSerializer *) __is;
- (void) __write: (GYSerializer *) __os;
- (id) copyWithZone: (NSZone *) zone;
@end


// ITest_getIntList_response
@interface ITest_getIntList_response: GYRmiResponseBase
- (id) init;

#pragma mark - overridden methods
- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) what code: (int) code;
- (void) __onTimeout;

#pragma mark - class-special methods
- (void) onResponseWithIntList: (SeqInt *) intList;
- (void) onError: (NSString *) what code: (GYInt) code;
- (void) onTimeout;
@end


// ITest_getDictIntString_response
@interface ITest_getDictIntString_response: GYRmiResponseBase
- (id) init;

#pragma mark - overridden methods
- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) what code: (int) code;
- (void) __onTimeout;

#pragma mark - class-special methods
- (void) onResponseWithIntStrMap: (DictIntString *) intStrMap;
- (void) onError: (NSString *) what code: (GYInt) code;
- (void) onTimeout;
@end


// ITest_getFloatList_response
@interface ITest_getFloatList_response: GYRmiResponseBase
- (id) init;

#pragma mark - overridden methods
- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) what code: (int) code;
- (void) __onTimeout;

#pragma mark - class-special methods
- (void) onResponseWithFloatList: (SeqFloat *) floatList andDummy: (GYInt) dummy;
- (void) onError: (NSString *) what code: (GYInt) code;
- (void) onTimeout;
@end


// ITest_signup_response
@interface ITest_signup_response: GYRmiResponseBase
- (id) init;

#pragma mark - overridden methods
- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) what code: (int) code;
- (void) __onTimeout;

#pragma mark - class-special methods
- (void) onResponseWithLoginReturn: (SLoginReturn *) loginReturn;
- (void) onError: (NSString *) what code: (GYInt) code;
- (void) onTimeout;
@end


// ITest_doNothing_response
@interface ITest_doNothing_response: GYRmiResponseBase
- (id) init;

#pragma mark - overridden methods
- (void) __onResponse: (GYSerializer *) __is;
- (void) __onError: (NSString *) what code: (int) code;
- (void) __onTimeout;

#pragma mark - class-special methods
- (void) onResponse;
- (void) onError: (NSString *) what code: (GYInt) code;
- (void) onTimeout;
@end


// ITestProxy
@interface ITestProxy: GYRmiResponseBase
- (id) init;

- (void) getIntListWithResponse: (ITest_getIntList_response *) __response andSize: size;
- (void) getDictIntStringWithResponse: (ITest_getDictIntString_response *) __response andSize: size;
- (void) getFloatListWithResponse: (ITest_getFloatList_response *) __response andSize: size;
- (void) signupWithResponse: (ITest_signup_response *) __response andSignup: signup;
- (void) doNothingWithResponse: (ITest_doNothing_response *) __response;
@end



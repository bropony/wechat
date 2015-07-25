//
//  GYSerializingError.h
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import <Foundation/Foundation.h>

@interface GYSerializingError : NSException
@property (copy, nonatomic) NSString * what;
@property int code;

- (id) init;
- (id) initWhat: (NSString *)what andCode:(int)code;
@end

//
//  GYSerializingError.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYSerializingError.h"

@implementation GYSerializingError
- (id) init
{
    self = [super init];
    if (self)
    {
        return [self initWhat:@"" andCode: 0];
    }
    
    return self;
}

- (id) initWhat:(NSString *)what andCode:(int)code
{
    self = [super init];
    
    if (self)
    {
        _what = what;
        _code = code;
    }
    
    return self;
}
@end

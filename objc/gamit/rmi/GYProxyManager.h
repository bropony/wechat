//
//  GYProxyManager.h
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import <Foundation/Foundation.h>
#import "GYRmiCore.h"

@interface GYProxyManager : NSObject
+ (GYProxyManager *) instance;

- (void) addProxy: (GYRmiProxyBase *) proxy;
- (GYRmiProxyBase *) getProxy: (NSString *) name;
@end

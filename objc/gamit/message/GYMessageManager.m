//
//  GYMessageManager.m
//  objc
//
//  Created by MaHanzhou on 7/15/15.
//
//

#import "GYMessageManager.h"

static GYMessageManager * gMessageManagerInstance = nil;

@interface GYMessageManager()
- (id) init;
@end

@implementation GYMessageManager
{
    NSMutableDictionary * _commandDict;
}

+ (GYMessageManager *) instance
{
    if (!gMessageManagerInstance)
    {
        gMessageManagerInstance = [[GYMessageManager alloc] init];
    }
    
    return gMessageManagerInstance;
}

- (id) init
{
    self = [super init];
    
    if (self)
    {
        _commandDict = [[NSMutableDictionary alloc] init];
    }
    
    return self;
}

- (void) registCommand: (int) command withHandler: (id<GYMessageBaseProtocol>) handler
{
    NSNumber * key = [NSNumber numberWithInt: command];
    
    [_commandDict setObject: handler forKey: key];
}

- (void) onMessage: (GYSerializer *) __is
{
    GYMessageBlock * msgBlock = [[GYMessageBlock alloc] initWithData: __is];
    
    GYInt command = [msgBlock command];
    NSNumber * key = [NSNumber numberWithInt: command];
    
    id<GYMessageCommandHandlerProtocal> commandHandler = [_commandDict objectForKey: key];
    if (commandHandler)
    {
        [commandHandler onMessage: msgBlock];
    }
}

@end

//
//  GYSerializer.m
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import "GYSerializer.h"
#import "GYSerializingError.h"

static const char VERSION = 1;

#define LENGTH_OF_BYTE 1
#define LENGTH_OF_BOOL 1
#define LENGTH_OF_SHORT 2
#define LENGTH_OF_INT 4
#define LENGHT_OF_LONG 8
#define LENGTH_OF_FLOAT 4
#define LENGHT_OF_DOUBLE 8

@implementation GYSerializer
{
    NSMutableData* _buffer;
    int _currentPos;
}

- (id) init
{
    self = [super init];
    
    if (NULL != self)
    {
        _buffer = [[NSMutableData alloc] init];
        _currentPos = 0;
    }
    
    return self;
}

- (id) initWithData:(NSData *)data
{
    self = [super init];
    
    if (NULL == self)
    {
        _buffer = [[NSMutableData alloc] initWithData: data];
        _currentPos = 0;
    }
    
    return self;
}

- (void) startToRead
{
    GYByte ver = [self readByte];
    
    if (ver != VERSION)
    {
        GYSerializingError * sError = [[GYSerializingError alloc] initWhat: @"SerialingVersionNotMatched" andCode: 0];
        @throw sError;
    }
}

- (void) startToWrite
{
    [self writeByte: VERSION];
}

- (NSData *) getBuffer
{
    return _buffer;
}

- (void) writeBytes:(const void *)bytes withLenght:(unsigned int)legnth
{
    [_buffer appendBytes: bytes length: legnth];
}

- (NSData *)readBytesWithLength:(unsigned int)length
{
    void * bytes = malloc(length);
    NSRange range = NSMakeRange(_currentPos, length);
    
    [_buffer getBytes: bytes range: range];
    NSData * data = [[NSData alloc] initWithBytes: bytes length: length];
    
    _currentPos += length;
    
    return data;
}

- (void) readBytes: (void *) data withLength: (unsigned int) length;
{
    NSRange range = NSMakeRange(_currentPos, length);
    
    [_buffer getBytes: data range: range];
    
    _currentPos += length;
}

- (GYBool) readBool
{
    GYBool bVal = NO;
    
    [self readBytes: &bVal withLength: LENGTH_OF_BOOL];
    
    return bVal;
}

- (void) writeBool:(GYBool)bVal
{
    [_buffer appendBytes: &bVal length: LENGTH_OF_BOOL];
}

- (GYByte) readByte
{
    GYByte byVal = 0;
    
    [self readBytes: &byVal withLength: LENGTH_OF_BYTE];
    
    return byVal;
}

- (void) writeByte:(GYByte)byVal
{
    [_buffer appendBytes: &byVal length: LENGTH_OF_BYTE];
}

- (GYShort) readShort
{
    GYShort sVal = 0;
    
    [self readBytes: &sVal withLength: LENGTH_OF_SHORT];
    
    sVal = CFSwapInt16LittleToHost(sVal);
    
    return sVal;
}

- (void) writeShort:(GYShort)sVal
{
    sVal = CFSwapInt16HostToLittle(sVal);
    
    [_buffer appendBytes: &sVal length: LENGTH_OF_SHORT];
}

- (GYInt) readInt
{
    GYInt iVal = 0;
    
    [self readBytes: &iVal withLength: LENGTH_OF_INT];
    
    iVal = CFSwapInt32LittleToHost(iVal);
    
    return iVal;
}

- (void) writeInt:(GYInt)iVal
{
    iVal = CFSwapInt32HostToLittle(iVal);
    
    [_buffer appendBytes: &iVal length: LENGTH_OF_INT];
}

- (GYLong) readLong
{
    GYLong lVal = 0;
    
    [self readBytes: &lVal withLength: LENGHT_OF_LONG];
    
    lVal = CFSwapInt64LittleToHost(lVal);
    
    return lVal;
}

- (void) writeLong:(GYLong)lVal
{
    lVal = CFSwapInt64HostToLittle(lVal);
    
    [_buffer appendBytes: &lVal length: LENGHT_OF_LONG];
}

- (GYFloat) readFloat
{
    GYFloat fVal = 0.0;
    
    [self readBytes: &fVal withLength: LENGTH_OF_FLOAT];
    
    fVal = CFSwapInt32LittleToHost(fVal);
    
    return fVal;
}

- (void) writeFloat:(GYFloat)fVal
{
    fVal = CFSwapInt32HostToLittle(fVal);
    
    [_buffer appendBytes: &fVal length: LENGTH_OF_FLOAT];
}

- (GYDouble) readDouble
{
    GYDouble dbVal = 0.0;
    
    [self readBytes: &dbVal withLength: LENGHT_OF_DOUBLE];
    
    dbVal = CFSwapInt64LittleToHost(dbVal);
    
    return dbVal;
}

- (void) writeDouble:(GYDouble)dbVal
{
    dbVal = CFSwapInt64HostToLittle(dbVal);
    
    [_buffer appendBytes: &dbVal length: LENGHT_OF_DOUBLE];
}

- (NSString *) readString
{
    int strLen = [self readInt];
    
    NSData * bytes = [self readBytesWithLength: strLen];
    NSString * str = [[NSString alloc] initWithData: bytes encoding: NSUTF8StringEncoding];
    
    return str;
}

- (void) writeString:(NSString *)str
{
    GYLong strLen = [str length];
    NSData * data = [str dataUsingEncoding: NSUTF8StringEncoding];
    
    [self writeInt: (int)strLen];
    [_buffer appendData: data];
}

- (NSDate *) readDate
{
    GYLong secs = [self readLong];
    
    NSDate * date = [NSDate dateWithTimeIntervalSince1970: secs];
    
    return date;
}

- (void) writeDate:(NSDate *)date
{
    GYLong secs = [date timeIntervalSince1970];
    
    [self writeLong: secs];
}

- (NSData *) readBinary
{
    GYInt binLength = [self readInt];
    
    NSData * data = [self readBytesWithLength: binLength];
    
    return data;
}

- (void) writeBinary:(NSData *)binary
{
    NSUInteger dataLen = [binary length];
    
    [self writeInt: (GYInt)dataLen];
    [_buffer appendData: binary];
}

- (void) __mask
{
    char mask = 108;
    
    NSUInteger length = [_buffer length];
    if (0 == length)
    {
        return;
    }
    
    NSUInteger maxIdx = length - 1;
    char * bytes = (char *)[_buffer bytes];
    
    for (NSUInteger i = 0; i <= maxIdx; i += 2)
    {
        if (i == maxIdx)
        {
            bytes[i] ^= mask;
            return;
        }
        
        char bi = bytes[i];
        char bj = bytes[i + 1];
        
        bi ^= mask;
        bj ^= mask;
        
        bytes[i] = bj;
        bytes[i + 1] = bi;
    }
}

- (void) __encrypt
{
    NSUInteger length = [_buffer length];
    
    if (0 == length)
    {
        return;
    }
    
    char pivot = (char)(arc4random() % 127) + 1;
    [self writeByte: pivot];
    
    char * bytes = (char *)[_buffer bytes];
    
    for (long i = length - 1; i >= 0; --i)
    {
        bytes[i] ^= pivot;
        pivot = bytes[i];
    }
}

- (void) __decrypt
{
    NSUInteger length = [_buffer length];
    
    if (0 == length)
    {
        return;
    }
    
    char * bytes = (char *)[_buffer bytes];
    
    for (NSUInteger i = 0; i < length - 1; i++)
    {
        bytes[i] ^= bytes[i + 1];
    }
    
    [_buffer setLength: [_buffer length] - 1];
}

- (void) simpleEncrypt
{
    [self __mask];
    [self __encrypt];
}

- (void) simpleDecrypt
{
    [self __decrypt];
    [self __mask];
}
@end

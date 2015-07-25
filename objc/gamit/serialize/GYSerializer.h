//
//  GYSerializer.h
//  objc
//
//  Created by MaHanzhou on 7/14/15.
//
//

#import <Foundation/Foundation.h>
#import "GYDef.h"

@interface GYSerializer : NSObject

#pragma mark - initiations
- (id) init;
- (id) initWithData: (NSData*) data;

#pragma mark - preparations
- (void) startToRead;
- (void) startToWrite;

#pragma mark - retrieve utils
- (NSData *) getBuffer;

#pragma mark - read and write utils
- (void) writeBytes: (const void *) bytes withLenght: (unsigned int) legnth;
- (NSData *) readBytesWithLength: (unsigned int) length;
- (void) readBytes: (void *) data withLength: (unsigned int) length;

- (GYBool) readBool;
- (void) writeBool: (GYBool) bVal;

- (GYByte) readByte;
- (void) writeByte: (GYByte) byVal;

- (GYShort) readShort;
- (void) writeShort: (GYShort) sVal;

- (GYInt) readInt;
- (void) writeInt: (GYInt) iVal;

- (GYLong) readLong;
- (void) writeLong:(GYLong) lVal;

- (GYFloat) readFloat;
- (void) writeFloat: (GYFloat) fVal;

- (GYDouble) readDouble;
- (void) writeDouble: (GYDouble) dbVal;

- (NSString *) readString;
- (void) writeString: (NSString *) str;

- (NSDate *) readDate;
- (void) writeDate: (NSDate *) date;

- (NSData *) readBinary;
- (void) writeBinary: (NSData *) binary;

#pragma mark - encryption and decryption
- (void) __mask;
- (void) __encrypt;
- (void) __decrypt;
- (void) simpleEncrypt;
- (void) simpleDecrypt;

@end

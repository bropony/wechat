package rmi;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Date;
import java.util.Random;

public class Serializer {
	final public byte VERSION = 1;
	
    final public static byte RmiDataCall = 1;
	final public static byte RmiDataResponse = 2;
	final public static byte RmiDataMessageBlock = 3;
	final public static byte RmiDataException = 4;
	
	final public int SIZE_OF_BYTE = 1;
	final public int SIZE_OF_SHORT = 2;
	final public int SIZE_OF_INT = 4;
	final public int SIZE_OF_LONG = 8;
	final public int SIZE_OF_FLOAT = 4;
	final public int SIZE_OF_DOUBLE = 8;
	
	private ByteBuffer _buffer;
	private int _bufferSize;
	private int _dataSize;
	private boolean _hasStartedReading = false;
	private boolean _hasStartedWriting = false;
	
	public Serializer(){
		_dataSize = 0;
		_bufferSize = 256;
		_buffer = createNewBuffer(_bufferSize);
		_buffer.order(ByteOrder.LITTLE_ENDIAN);
	}
	
	public Serializer(ByteBuffer bb){
		_buffer = bb;
		_dataSize = bb.remaining();
		_buffer.order(ByteOrder.LITTLE_ENDIAN);
		_bufferSize = _dataSize;
	}
	
	public Serializer(byte[] bs){
		ByteBuffer bb = ByteBuffer.wrap(bs);
		
		_buffer = bb;
		_dataSize = bb.remaining();
		_buffer.order(ByteOrder.LITTLE_ENDIAN);
		_bufferSize = _dataSize;
	}
	
	public void startToWrite(){
		if (_hasStartedWriting){
			return;
		}
		
		write(VERSION);
		_hasStartedWriting = true;
	}
	
	public void startToRead(){
		if (_hasStartedReading){
			return;
		}
		
		byte version = readByte();
		if (version != VERSION){
			System.out.println("[SerializeStream]DataVersionNotMatched");
		}
		
		_hasStartedReading = true;
	}
	
	public byte[] getBytes(){
		if (0 == _dataSize){
			return null;
		}
		byte[] res = new byte[_dataSize];
		_buffer.flip();
		_buffer.get(res, 0, _dataSize); 
		
		return res;
	}
	
	static public ByteBuffer createNewBuffer(int bufferSize){
		byte[] b = new byte[bufferSize];
		ByteBuffer bb = ByteBuffer.wrap(b);
		bb.order(ByteOrder.LITTLE_ENDIAN);
		
		return bb;
	}
	
	private void increSize(int size){	
		if (_dataSize + size > _bufferSize){
			_bufferSize = 2 * (_dataSize + size);
			
			ByteBuffer newBuffer = createNewBuffer(_bufferSize);
			
			byte[] data = getBytes();
			if (null != data)
			{
				newBuffer.put(data);
			}
			
			_buffer = newBuffer;
		}
		
		_dataSize += size;
	}
	
	//byte
	public void write(byte b){
		increSize(SIZE_OF_BYTE);

		_buffer.put(b);
	}
	
	public void write(byte[] ba){
		write(ba.length);
		
		for (int i = 0; i < ba.length; ++i){
			write(ba[i]);
		}
	}
	
	public void write(byte[][] baa){
		write(baa.length);
		for (int i = 0; i < baa.length; ++i){
			write(baa[i]);
		}
	}
	
	public byte readByte(){
		return _buffer.get();
	}
	
	public byte read(byte res){
		return _buffer.get();
	}
	
	public byte[] readBytes(){
		int size = readInt();
		byte[] bytes = new byte[size];
		
		for (int i = 0; i < size; i++){
			bytes[i] = readByte();
		}
		
		return bytes;
	}
	
	public byte[] read(byte[] res){
		res = readBytes();
		return res;
	}
	
	public byte[][] read(byte[][] res){
		int size = readInt();
		res = new byte[size][];
		for (int i = 0; i < size; i++){
			res[i] = read(res[i]);
		}
		return res;
	}
	
	//boolean
	public void write(boolean b){
		byte val = 0;
		if (b){
			val = 1;
		}
		write(val);
	}
	
	public void write(boolean[] ba){
		write(ba.length);
		
		for (int i = 0; i < ba.length; ++i){
			write(ba[i]);
		}
	}
	
	public boolean readBool(){
		byte val = readByte();
		if (val != 0){
			return true;
		}
		else{
			return false;
		}
	}
	
	public boolean read(boolean res){
		res = readBool();
		return res;
	}
	
	public boolean[] readBools(){
		int size = readInt();
		boolean[] res = new boolean[size];
		
		for (int i = 0; i < size; i++){
			res[i] = readBool();
		}
		
		return res;
	}
	
	public boolean[] read(boolean[] res){
		res = readBools();
		return res;
	}
	
	
	//short
	public void write(short s){
		increSize(SIZE_OF_SHORT);
		
		_buffer.putShort(s);
	}
	
	public void write(short[] sa){
		write(sa.length);
		
		for (int i = 0; i < sa.length; ++i){
			write(sa[i]);
		}
	}
	
	public short readShort(){
		return _buffer.getShort();
	}
	
	public short read(short res){
		res = readShort();
		return res;
	}
	
	public short[] readShorts(){
		int size = readInt();
		short[] res = new short[size];
		
		for (int i = 0; i < size; i++){
			res[i] = readShort();
		}
		
		return res;
	}
	
	public short[] read(short[] res){
		res = readShorts();
		return res;
	}
	
	//int
	public void write(int i){
		increSize(SIZE_OF_INT);
		
		_buffer.putInt(i);
	}
	
	public void write(int[] ia){
		write(ia.length);
		
		for (int i = 0; i < ia.length; ++i){
			write(ia[i]);
		}
	}
	
	public int readInt(){
		return _buffer.getInt();
	}
	
	public int read(int res){
		res = readInt();
		return res;
	}
	
	public int[] readInts(){
		int size = readInt();
		int[] res = new int[size];
		
		for (int i = 0; i < size; i++){
			res[i] = readInt();
		}
		
		return res;
	}
	
	public int[] read(int[] res){
		res = readInts();
		return res;
	}
	
	//long
	public void write(long l){
		increSize(SIZE_OF_LONG);
		
		_buffer.putLong(l);
	}
	
	public void write(long[] la){
		write(la.length);
		
		for (int i = 0; i < la.length; ++i){
			write(la[i]);
		}
	}
	
	public long readLong(){
		return _buffer.getLong();
	}
	
	public long read(long res){
		res = readLong();
		return res;
	}
	
	public long[] readLongs(){
		int size = readInt();
		long[] res = new long[size];
		
		for (int i = 0; i < size; ++i){
			res[i] = readLong();
		}
		
		return res;
	}
	
	public long[] read(long[] res){
		res = readLongs();
		return res;
	}
	
	//float
	public void write(float f){
		increSize(SIZE_OF_FLOAT);
		
		_buffer.putFloat(f);
	}
	
	public void write(float[] fa){
		write(fa.length);
		
		for (int i = 0; i < fa.length; ++i){
			write(fa[i]);
		}
	}
	
	public float readFloat(){
		return _buffer.getFloat();
	}
	
	public float read(float res){
		res = readFloat();
		return res;
	}
	
	public float[] readFloats(){
		int size = readInt();
		float[] res = new float[size];
		
		for (int i = 0; i < size; ++i){
			res[i] = readFloat();
		}
		
		return res;
	}
	
	public float[] read(float[] res){
		res = readFloats();
		return res;
	}
	
	//double
	public void write(double d){
		increSize(SIZE_OF_DOUBLE);
		
		_buffer.putDouble(d);
	}
	
	public void write(double[] da){
		write(da.length);
		
		for (int i = 0; i < da.length; ++i){
			write(da[i]);
		}
	}
	
	public double readDouble(){
		return _buffer.getDouble();
	}
	
	public double read(double res){
		res = readDouble();
		return res;
	}
	
	public double[] readDoubles(){
		int size = readInt();
		double[] res = new double[size];
		
		for (int i = 0; i < size; ++i){
			res[i] = readDouble();
		}
		
		return res;
	}
	
	public double[] read(double[] res){
		res = readDoubles();
		return res;
	}
	
	//Date
	public void write(Date dt){
		write(dt.getTime());
	}
	
	public void write(Date[] dta){
		write(dta.length);
		
		for (int i = 0; i < dta.length; ++i){
			write(dta[i]);
		}
	}
	
	public Date readDate(){
		long dtTime = readLong();
		
		Date dt = new Date(dtTime);
		
		return dt;
	}
	
	public Date read(Date res){
		res = readDate();
		return res;
	}
	
	public Date[] readDates(){
		int size = readInt();
		Date[] res = new Date[size];
		
		for (int i = 0; i < size; i++){
			res[i] = readDate();
		}
		
		return res;
	}
	
	public Date[] read(Date[] res){
		res = readDates();
		return res;
	}
	
	//string
	public void write(String s){
		//byte[] bytes = s.getBytes(StandardCharsets.UTF_8);
		//write(bytes);
		
		try{
			byte[] bytes = s.getBytes("UTF-8");
			write(bytes);
		}
		catch (Exception e){
			e.printStackTrace();
		}
	}
	
	public void write(String[] sa){
		write(sa.length);
		
		for (int i = 0; i < sa.length; ++i){
			write(sa[i]);
		}
	}
	
	public String readString(){
		byte[] bytes = readBytes();
		//String res = new String(bytes, StandardCharsets.UTF_8);
		
		String res = "";
		try{
			res = new String(bytes, "UTF-8");
		}
		catch (Exception e){
			e.printStackTrace();
		}
		
		return res;
	}
	
	public String read(String res){
		res = readString();
		return res;
	}
	
	public String[] readStrings(){
		int size = readInt();
		String[] res = new String[size];
		
		for (int i = 0; i < size; i++){
			res[i] = readString();
		}
		
		return res;
	}
	
	public String[] read(String[] res){
		res = readStrings();
		return res;
	}
	
	private void __mask()
	{
		byte mask = 108;
		
		if (_dataSize == 0)
		{
			return;
		}
		
		int maxIdx = _dataSize - 1;
		byte[] data = _buffer.array();
		
		for (int i = 0; i <= maxIdx; i += 2)
		{
			if (i == maxIdx)
			{
				data[i] ^= mask;
				return;
			}
			
			byte bi = data[i];
			byte bj = data[i + 1];
			
			bi ^= mask;
			bj ^= mask;
			
			data[i] = bj;
			data[i + 1] = bi;
		}
	}
	
	private void __encrypt()
	{
		if (_dataSize == 0)
		{
			return;
		}
		
		Random r = new Random();
		byte pivot = (byte)(r.nextInt(127) + 1);
		this.write(pivot);
		
		byte[] data = _buffer.array();
		for (int i = data.length - 1; i >= 0; --i)
		{
			data[i] ^= pivot;
			pivot = data[i];
		}
	}
	
	private void __decrypt()
	{
		if (_dataSize == 0)
		{
			return;
		}
		
		byte[] data = _buffer.array();
		for (int i = 0; i < data.length - 1; i++)
		{
			data[i] ^= data[i + 1];
		}
	}
	
	public void simpleEncrypt()
	{
		__mask();
		__encrypt();
	}
	
	public void simpleDecrypt()
	{
		__decrypt();
		__mask();
	}
}

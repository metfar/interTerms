#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  math_h.py
#  
#  Copyright 2021 William Martinez Bas <metfar@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  This is part of WalSoc Project < https://github.com/metfar/walsoc/tree/master/walsoc/pa >

try:
	ALIAS_H;
except NameError:
	from alias_h import * ;
try:
	STRING_H;
except NameError:
	from string_h import * ;

MATH_H=TRUE;

import math;
from sys import version;
#from math import sin, cos,sqrt;

PI=pi=PI=3.141592653589793;	#(2**0.5)*2.221441469079;#3.1415926535895347
e=2.718281828459045; 		#((pi**4)+(pi**5))**(1/6);#2.7182818086117377
phi=1.618033988749895;          #phi=0.5+(5**(0.5))*0.5; Golden ratio
infinite=None;#math.inf;


def toRad(ang):
	"""
	Math Function
	-------------
	
	Converts degrees into radians.
	
	toRad(180) 
			returns 3.1415927 (PI)
	"""
	return(ang*pi/180.0);
def toDeg(ang):
	"""
	Math Function
	-------------
	
	Converts radians into degrees.
	
	toDeg(pi) 
			returns 180 (degrees)
	"""
	return(ang*180.0/pi);
	
def toFloat(inp):
	"""
	Convert first ocurrency of numeric value 
	into a floating point number
	
	toFloat(" la casa roja 3.2 180 ")
			
			ANS: 3.2
	"""
	out=0.0;
	x=sprintf("%s",inp).strip();
	for f in x.split():
		try:
			tmp=(type(float(f))==type(1.1));
			
		except:
			tmp=false;
		
		if (tmp):
			out=float(f);
			break;
	return(out);

def toInt(inp):
	return(int(toFloat(inp)));
	
#round native


def sin(ang):
	"""
	Math Function
	-------------
	
	Returns the Sine value of n-degrees angle.
	
	sin(90)
			returns 1
	"""
	return(math.sin(toRad(ang)));#(round(math.sin(toRad(ang)),8));

def sinh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic sine value of n-degrees angle.
	
	sinh(90)
			returns 2.30129896
	"""
	return (math.sinh(toRad(ang))); #(round(math.sinh(toRad(ang)),8));
	
def asin(val):
	"""
	Math Function
	-------------
	
	Returns the arc Sine value of n (-1<=n<=1).
	
	asin(1)
			returns 90
	"""
	return(toDeg(math.asin(val)));

def asinh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic arc sine value of n.
	
	asinh(2.301298960533041)
			returns 90
	"""
	return(toDeg(math.asinh(val)));

def cos(ang):
	"""
	Math Function
	-------------
	
	Returns the Cosine value of n-degrees angle.
	
	cos(0)
			returns 1
	"""
	return(math.cos(toRad(ang)));

def cosh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	cosh(90)
			returns 2.50917853
	"""
	return(math.cosh(toRad(ang)));
	
def acos(val):
	"""
	Math Function
	-------------
	
	Returns the arc Cosine value of n.
	
	acos(0)
			returns 0
	"""
	dm=0;#val/2*.0000000075; used in early versions with rounded values
	return(toDeg(math.acos(val+dm)));

def acosh(val):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic Cosine value of n-degrees angle.
	
	acosh(2.50917853)
			returns 90
	"""
	dm=0;#.0000000005
	return(toDeg(math.acosh(val)+dm));


def tan(ang):
	"""
	Math Function
	-------------
	
	Returns the tangent value of n-degrees angle.
	
	tan(45)
			returns 1
	"""
	return(math.tan(toRad(ang)));

def atan(val):
	"""
	Math Function
	-------------
	
	Returns the arc tangent in degrees.
	
	atan(1)
			returns 45
	"""
	
	return(toDeg(math.atan(val)));

def tanh(ang):
	"""
	Math Function
	-------------
	
	Returns the hyperbolic tangent value of n-degrees angle.
	
	tan(45)
			returns 0.65579421
	"""
	return(math.tanh(toRad(ang)));
	
def atanh(val):
	"""
	Math Function
	-------------
	
	Returns the angle of an hyperbolic tangent arc value.
	
	atanh(0.65579421)
			returns 45.0
	"""
	return(toDeg(math.atanh(val)));


def atan2(y,x):
	"""
	Math Function
	-------------
	
	Returns the arc tangent of y/x in degrees.
	
	atan2(1,1)
			returns 45
	"""
	
	return(toDeg(math.atan2(y,x)));

def sqrt(num,y=2):
	"""
	Math Function
	-------------
	
	Returns the square root of a number (precision 8).
	
	sqrt(2)		returns 1.41421354
	sqrt(2,3)		returns 1.25992105
	sqrt(2,3,2)	returns 1.26
	
	"""
	num=toFloat(num);
	if(toFloat(y)==0.0):
		xraise("SQRT 0 of "+str(num)+" is undefined!");
		return(null);
	else:
		try:
			invers=1/y;
			return(math.pow(num,invers));
		except:
			try:
				return(math.sqrt(num));
			except:
				return(0.0);


sqr=sqrt;


def bin2dec(num):
	"""
	Math Function
	-------------
	
	Binary to decimal:
	
	bin2dec('10101010')
		
			returns 170
	
	"""
	return(int(num,2));

def oct2dec(num):
	"""
	Math Function
	-------------
	
	Octal to decimal:
	
	oct2dec('063')
		returns 51
	
	"""
	return(int(num,8));

def hexToDec(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to decimal:
	
	hexToDec('0F')
		returns 15
	
	"""
	return(int(num,16));

def hexToBList(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to Bytes List:
	
	hex2List("fffff")
		returns (15,255,255);
	"""
	out=[];
	if(len(num)%2==1):
		num="0"+str(num);
	
	for f in range(0,len(num),2):
		out.append(int(num[f:f+2],16));
	return(out);

def decToBin(inp):
	"""
	Math Function
	-------------
	
	Decimal to Binary:
	
	decToBin(138)
	
		returns '10001010'
	"""
	num=toInteger(inp);
	return(bin(num)[2:]);
	
def decToHex(inp):
	"""
	Math Function
	-------------
	
	Decimal to Hexadecimal:
	
	decToHex(16383000)
	
		returns 'f9fc18'
	"""
	num=toInteger(inp);
	return(hex(num)[2:]);

def hexToBList(num):
	"""
	Math Function
	-------------
	
	Hexadecimal to Bytes List:
	
	hexToBList('fffff')
		returns (15,255,255);
	"""
	out=[];
	num=str(num);
	if (len(num)%2==1):
		num="0"+num;

	for f in xrange(0,len(num),2):
		val=substr(num,f,2);
		out.append(int(val,16));

	return(out);


def decToBList(inp):
	"""
	Math Function
	-------------
	
	Decimal to bytes:
	
	decToBList(1638400)
		returns [25,0,0];
	"""
	out=[];
	while inp>255:
		ent=inp-(inp//256)*256;
		out.insert(0,ent);
		inp=inp//256;
	out.insert(0,inp);
	return(out);



def col(hexa):
	"""
	Math Function
	-------------
	
	col("ffffff") to tuple(r,g,b)
	
	"""
	out=decToBList(hexToDec(hexa));
	while len(out)<3:
		out.insert(0,0);
	return( out );
	

def pal(n):
	"""
	Math Function
	-------------
	
	pal		#Set default colours as global
	
	pal(1)	#Dark palette;
	
	pal()	#ZX_Spectrum-like palette;
	
	
	"""
	colnames=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "brightblack", "brightred", "brightgreen", "brightyellow", "brightblue", "brightmagenta", "brightcyan", "brightwhite"];
	
	n=toInt(n);
	if(n==1):
		COLVALUES=[	[0, 0, 0], [159, 0, 0], [0, 159, 0], [159, 159, 0], [0, 0, 159], [159, 0, 159], [0, 159, 159], [159, 159, 159], [36, 36, 36], [189, 0, 0], [0, 189, 0], [189, 189, 0], [0, 0, 189], [189, 0, 189], [0, 189, 189], [189, 189, 189]];

	else:
		COLVALUES=[[0, 0, 0], [215, 0, 0], [0, 215, 0], [215, 215, 0], [0, 0, 215], [215, 0, 215], [0, 215, 215], [215, 215, 215], [51, 51, 51], [255, 0, 2], [0, 255, 3], [253, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]];
	out=dict();
	for f in xrange(0,min(len(COLVALUES),len(colnames))):
		out[colnames[f]]=COLVALUES[f];
	#	return({"names":colnames,"values":COLVALUES});
	return(out);


def filterNum(string,sample="0123456789.-"):
	NUMS=[f for f in sample];
	tmp="".join([f if f in NUMS else "" for f in str(string)]);#Only numeric characters
	tmp=("-" if "-" in tmp else "")+tmp.replace("-","");#only - at start or nothing
	if(len(tmp)==0 or tmp=="-"):
		tmp="0";
	if(not("." in tmp)):
		tmp+=".0";
	return(tmp);

def toFPStruct(string):
	tmp=filterNum(string);
	if tmp[0]=="-":
		S=-1;
		tmp=tmp[1:];
	else:
		S=1;
	st="";
	pos=-1;
	i=0;
	for f in tmp:
		if f==".":
			pos=i;
		else:
			st+=f;
		i+=1;
	if(pos==-1):
		pos=len(st);
	Exp=pos-len(st);
	Fact=float(10.0**Exp);
	val=int(st);
	return([tmp,S*val*Fact,S,val,Exp]);

def toNum(string):
	tmp=toFPStruct(string);
	return(tmp[1]);

class FPoint:
	"""
		Floating Point Conversion Class
	"""
	def __init__(self,value=0):
		tmp=toFPStruct(value);
		self._value=tmp[1];
		self._string=tmp[0];
		self._sign=tmp[2];
		self._intval=tmp[3];
		self._exp=tmp[4];
	
	def __repr__(self):
		s=str(self._intval);
		e=self._exp;
		S="-" if self._sign<0 else " ";
		l=s[:8];
		if(len(s)>len(l)):
			e=e+len(s)-len(l);
		return(S+l+"×10^("+str(e)+")");

	def value(self):
		s=str(self._intval);
		e=self._exp;
		S="-" if self._sign<0 else " ";
		l=s[:8];
		if(len(s)>len(l)):
			e=e+len(s)-len(l);
		out=self._sign*int(l);
		e=10**e;
		return(out*e);
	
	def bin(self):
		s=str(self._intval);
		e=self._exp;
		l=s[:8];
		if(len(s)>len(l)):
			e=e+len(s)-len(l);
		s=bin(int(l) & 0xffffffff)[2:]; #s is a natural number 
										#from 0 to 4294967295 (4GB)
										#Now it is a binary string
		sExp="1" if e<0 else "0";
		sign="1" if self._sign<0 else "0";
		#print(sign);
		#print(sExp);
		e=abs(e) & 63;
		#print(e);
		out= sign;#first the sign of the value
		out+=sExp;#second the sign of the exponent
		out+=("%6s"%bin(int(abs(e)))[2:]).replace(" ","0");
		out+=("%32s"%s).replace(" ","0");
		return(out);
	
	def __eq__(self,other):
		if (type(self)!=type(other)):
			tmp=FPoint(other);
		else:
			tmp=other;
		out= (self.bin()==tmp.bin());
		#print(self.bin());
		#print(tmp.bin());
		return(out);
	
def ticktock(string,tick="√",tock="_",start="<",mid=".",end=">"):
	out="";
	s=str(string);
	i=0;
	for f in s:
		if(i%4==0):
			out+=mid;
		if(f=="0"):
			out+=tock;
		if(f=="1"):
			out+=tick;
		i+=1;
	out+=end;
	out=start+out;
	return(out);

def tactac(string):
	return(ticktock(string,tick="1",tock="0",start="[",mid=" ",end=" ]"));


def filterBin(string):
	return(filterNum(str(string).replace(".",""),"01-")[:-2]);
	
def filterHex(string):
	inp=str(string).replace(".","").upper();
	out=filterNum(inp,"0123456789ABCDEF-");
	
	return(out[:-2]);

def groupsOf(string,n=2,sep="."):
	return(sep.join(map("".join,zip(*[iter(string)]*n))));

def binToHex(string):
	return(groupsOf(hex(int(filterBin(string),2))[2:],2).upper());

def hexToBin(string):
	return(groupsOf(bin(int(filterHex(string),16))[2:],4));

	
def binToFP(string):
	out=0.0;
	a=binToHex(string).split(".");
	intval=int("".join(a[1:]),16);
	S=	 -1 if (0<(int(a[0],16) & 128)) else 1;
	sExp=-1 if (0<(int(a[0],16) & 64)) else 1;
	e=int(a[0],16) & 63;
	e=10**(sExp*e);
	
	return(FPoint(S*e*intval));

	
def pow(x,y=2):
	"""
	Math Function
	-------------
	
	pow(x,y)	returns x^y
	pow(x)	returns x^2
	
	"""
	if(y==0):
		return(1.0);
	elif (y==infinite):
		return(infinite);
	else:
		try:
			return(round(math.pow(num,y),digits));
		except:
			try:
				return(math.pow(num,y));
			except:
				printf("Error at power!");
				return(0.0);
	
def exp(x=1):
	"""
	Math Function
	-------------
	
	exp(x)	returns e^x
	
	"""
	try:
		return(math.pow(e,x));
	except:
		try:
			return(e**x);
		except:
			xraise("Error at e-exponential!");
	return(1.0);

def log(x=1):
	"""
	Math Function
	-------------
	
	log(2)	returns 0.30103 (log_10(x))
	
	"""
	if(toFloat(x)==0.0):
		return(-math.inf);
	try:
		return(math.log10(x));
	except:
		xraise("Error at 10-based logarythm!");
	return(0);

def ln(x=1,digits=8):
	"""
	Math Function
	-------------
	
	ln(2)	returns 0.69314718 (log_e(x))
	
	"""
	try:
		return(math.log(x));
	except:
		printf("Error at natural logarythm!");
		return(0);

def div(x,y=1):
	"""
	Math Function
	-------------
	
	div(3,2)	returns 1.5
	div(3,0)	returns infinite
	
	"""
	y=toFloat(y);
	x=toFloat(x);
	if(y==0.0):
		return(infinite);
	else:
		try:
			return(x/y);
		except:
			xraise("Error at division!");
	return(0.0);

def fabs(x,digits=8):
	"""
	Math Function
	-------------
	
	fabs(-3.33333)		returns 3.33333
	
	"""
	try:
		return(math.fabs(x));
	except:
		xraise("Error at fabs!");
	return(0.0);

def floor(num):
	"""
	Math Function
	-------------
	
	floor(-3.33333)	returns -4
	floor( 3.33333)	returns  3
	
	"""
	try:
		return(math.floor(num));
	except:
		printf("Error at floor!");
		return(0);
def ceil(num):
	"""
	Math Function
	-------------
	
	ceil(-3.33333)	returns -3
	
	ceil( 3.33333)	returns  4
	
	"""
	try:
		return(math.ceil(num));
	except:
		printf("Error at ceil!");
		return(0);

def fmod(x,y):
	"""
	Math Function
	-------------
	
	fmod(5,3.3)	returns -1.7
	
	fmod(10,3)	returns  1.0
	
	"""
	try:
		return(math.fmod(x,y));
	except:
		printf("Error at fmod!");
		return(0);

#min native
#max native


def main(args):
	
	echo (toRad(90));
	echo (sqr(2));
	echo (hexToBList("5384ff"));
	echo (decToBList(1638400));
	echo (pal(1));
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
else:
	pal(1);


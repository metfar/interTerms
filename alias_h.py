#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
#  alias_h.py
#  
#  Copyright 2020 William Martinez Bas <metfar@gmail.com>
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
  

import sys;
from os import getpid,path;
from asc_h import *;

#"constants"

ARGV=sys.argv;
nil=NULL=null=none=None;
ON=TRUE=true=True;
OFF=FALSE=false=False;
ECHO=ON;
GLUE=" ";
ALIAS_H=TRUE;
APP=ARGV[0];
PROCID=getpid();
FS=path.sep;
NAME=APP;
ENTER=enter=LF="\n";
EXCLAMATION="!";
LOADED=" loaded"+EXCLAMATION;
CORRECT_TYPES={
				"str":  "string",
				"int":  "integer",
				"bool": "boolean",
				"set":	"set"
				};

def List(*vargs):
	"""
			Define a list
	
	List()
			returns []
	
	List(1,['la','casa'],'roja')
			
			returns [1, ['la', 'casa'], 'roja']
	
	"""
	args=(vargs);
	out=[];
	for f in args:
		out.append(f);
	return(out);

	
def Dict(**vargs):
	"""
		Define dictionary
		
		Dict(a=1,b="casa")
	
					returns {'a': 1, 'b': 'casa'}

	"""
	try:    return ((vargs)[0]);
	except: return ((vargs));

def version():
	return(sys.version);


def procStr(x):
	out=x;
	try:
		if (x[0]=="'" and x[-1]=="'"):
			out=x[1:-1];#remove first and last simple quotation
	except:
		pass;
	return(out);
	
def echo(*vargs):
	"""
		GENERAL Function
		================
		
		if global ECHO is ON
			prints the argument and an ENTER
		else
			returns argument as a string
		
		It returns the string conversion of argument.
	"""
	global ECHO;
	try:
		ECHO;
	except:
		ECHO=ON;
	args=[];
	for f in vargs:
		if(type(f)==type(None)):
			args.append("null");
		elif(type(f)==type(True)):
			if(f==True):
				args.append("true");
			else:
				args.append("false");
		else:
			args.append(str(f));
	
	try:
		out=repr(args);
	except:
		out="";
		
	if(ECHO==ON):
		print(out[2:-2],end="");
		print(ENTER,end="");
		return(out);
	else:
		return(out);

#str is native
def sprintf(*vargs):
	""" 
	File Functions
	--------------
	
	stringOut= sprintf (FORMAT [,arg1,arg2,...]) 
	
	c-like sprintf
	
	"""
	
	global stderr;
	out="";
	args=list(vargs);
	try:
		Format=args.pop(0);
		out=(Format % tuple(args));
	except:
		print("Error on sprintf!",file=stderr);
	return(out);


def is_defined(x):
	"""
		GENERAL Function
		================
		is_defined (String)
		
		INP:    String:     variable name
		
		ANS:    Boolean:    exists in local or global scope
		
		
		is_defined("a")     corresponds to      is(defined? a)
	
	"""
	return ((x in locals()) or (x in globals()));

def toFloat(inp):
	"""
	GENERAL Function
	================
	
	toFloat converts the first numeric element of the input
			into a Float number and returns it or 0.0.
	"""
	
	out=0.0;
	x=sprintf("%s",inp).strip();
	for f in x.split():
		try:
			tmp=(type(float(f))==type(out));
		except:
			tmp=false;
		
		if (tmp):
			out=float(f);
			break;
	return(out);


def toInt(inp):
	"""
	GENERAL Function
	================
	toInt   returns the first numeric element of the input
			converted into an Integer, or 0.
	"""
	return(int(toFloat(inp)));


def count(inp):
	"""
	GENERAL Function
	================
	
	Number of elements from an object
	
	
	count(['la','123'])
					returns(2)
					
					
	count('casa')
					returns(4)
	
	"""
	return(len(inp));


class XRaise(Exception):
	def __init__(self, message=""):
		self.message = message;
		super().__init__(self.message);

def xraise(message="Error!"):
	raise XRaise(message);

def xrange(*vargs):
	"""
	GENERAL Function
	================
	
	xrange  requires 1 to 3 arguments(
			
	
	xrange(5)
			returns [0, 1, 2, 3, 4]
	
	xrange(2,10)
			returns [2, 3, 4, 5, 6, 7, 8, 9]
			
	xrange(2,10,3)
			returns [2,5,8]
			
	"""
	args=list(vargs);
	
	_step=0;
	_start=0;
	_stopBefore=nil;
	c=count(args);
	
	if (c==0):
			xraise("TypeError: xrange expected 1 argument, got 0");
	
	elif(c==1):
			_stopBefore=toInt(args[0]);
	elif(c==2):
			_start=toInt(args[0]);
			_stopBefore=toInt(args[1]);
	elif(c==3):
			_start=toInt(args[0]);
			_stopBefore=toInt(args[1]);
			_step=toInt(args[2]);
	else:
			xraise("TypeError: xrange expected at most 3 arguments, got "+str(c));
	
	if((_step>0 and _stopBefore<_start) or (_step<0 and _stopBefore>_start)):
		_stopBefore=_start;
	
	if(toInt(_step)==0):
		_step=1;
	
	out=[0];
	
	try:
		out=list(range(_start,_stopBefore,_step));
	except:
		pass;
	
	if (out[-1]==_stopBefore):
		out.pop(-1);
	return(out);


def popLast(inp):
	return(inp.pop(-1));
		
def pushLast(where,what):
	where.append(what);
	return(where.length);

def popFirst(inp):
	out=inp.pop(0);
	return(out);
	
def pushFirst(where,what):
	where.insert(0,what);
	return(where.length);

	
def isString(obj):
	return(type(obj)==type(""));

def isInteger(obj):
	return(type(obj)==type(1));


def isFloat(obj):
	return(type(obj)==type(1.0));

def isNumeric(obj):
	return(isFloat(obj) or isInteger(obj));

def isList(obj):
	return(type(obj)==type({}));

def isDict(obj):
	return(type(obj)==type({}));

def isIn(what,where):
	return(what in where);
	

def typeOf(input):
	cl=str(type(input));
	out=str(cl.split("'")[1]).lower();
	
	if(isIn(out,CORRECT_TYPES)):
		out=CORRECT_TYPES[out];
	elif(out.endswith(".set")):
		out="set";
	return(out);
PLANK_TIME=1.0E-43;

def main(*argv):
	echo(APP+LOADED);
        
	echo (is_defined("APP"));
	echo (xrange(5));
	echo (xrange(2,10));
	echo (xrange(2,10,3));
	echo ("La casa roja");
	a=List(1,2,3);
	echo(popLast(a));
	echo(popLast(a));
	echo(a);
	echo(typeOf(a));
	print (ascToIntl("¡El murciélago veloz del año comió pingüinos con Garçía!")+"\n");

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));

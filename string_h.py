#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  string_h.py
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
import os;
from alias_h import *;

STRING_H=True;

def array(*args, **kwargs):
    n=0;
    res=list();
    for a in args:
        res.append(a);
    return(res);


def toUpper(string):
    a="";
    try:
        a=a+string.upper();
    except:
        pass;
    return(a);
    

def toLower(string):
    a="";
    try:
        a=a+string.lower();
    except:
        pass;
    return(a);

def toCaps(string):
    a="";
    try:
        a=a+string.capitalize();
    except:
        pass;
    return(a);

def split(delimiter=" ",String="",limit=null):
    out=[];
    try:
       _tmp=str(String).split(delimiter);
       if(is_null(limit)):
             return(_tmp[:]);
       else:
             if(limit==-1):
                return(_tmp[:]);
             else:
                (limit+1)
        
    except:
          pass;
    return(out);
    

def join(glue=" ",arrayIn=[]):
    a=glue;b=arrayIn;
    try:
        return(a.join(b));
    except:
        try:
            return(b.join(a));
        except:
            return("");


def toTitle(string):
    a="";
    try:
        a=a+string.title();
    except:
        pass;
    return(a);

def endsWith(text,endWith=""):
    out=False;
    if(len(endWith)>0 and len(text)>len(endWith)):
        if(substr(text,-len(endWith))==endWith):
            out=true;
    return(out);

def basename(path,end=""):
    out=os.path.basename(path);
    if(len(end)>0):
       out=(out if not out.endswith(end) else out[:-strlen(end)]);
    return(out);

def dirname(path):
    return(os.path.dirname(path));

def allTrim(string):
    out=string;
    try:
        out=string.strip();
    except:
        pass;
    return(out);

def rTrim(string):
    out=string;
    try:
        out=string.rstrip();
    except:
        pass;
    return(out);


def lTrim(string):
    out=string;
    try:
        out=string.lstrip();
    except:
        pass;
    return(out);

def left(string,nChars):
    out="";
    if(nChars>len(string)):  
        out=str(string);
    elif (nChars>0):
        out=""+str(string);
        out=out[0:int(nChars)];
    return(out);

def right(string,nChars):
    out="";
    if(nChars>len(string)):  
        out=str(string);
    elif (nChars>0):
        out=""+str(string);
        n=len(string)-nChars;
        out=out[n:];
    return(out);

def substr(string, start, nChars = null):
        out="";
        if (start<0):
            start=start + len(string);
        if (nChars==null):
            out=string[start:];
        elif (nChars > 0):
            out=string[start:(start + nChars)];
        else:
            out=string[start:nChars];
        return(out);

def tr(string,characters,replacements):
	tmp=str(string);
	what=str(characters);
	forwhich=str(replacements);
	return(tmp.replace(what,forwhich));

def tr_d(string,characters):
	what=str(characters);
	return(tr(string,what,''));

def rev(string):
	i=string;
	if(typeOf(i)=="string"):
		o="";
		for x in range(len(i)-1,-1,-1): 
			o+=i[x];
	elif(typeOf(i)=="list"):
		o=[];
		for x in range(len(i)-1,-1,-1): 
			o.append(i[x]);
	else:
		o=i;
	return(o);

#len native
		
def strtok(string,delimiter=" "):
	return(split(delimiter,string));
	

def mid(string,start,nChars):
    out=right(string,len(string)-start);
    out=left(out,nChars);
    return(out);

def isString(obj):
    return(type(obj)==type(""));

def isInteger(obj):
    return(type(obj)==type(1));


def isFloat(obj):
    return(type(obj)==type(1.0));

def isNumeric(obj):
    return(isFloat(obj) or isInteger(obj));

def isIterable(obj):
    """
    isIterable  returns True if it has length
    """
    out=False;
    try:
        iter(obj);
        out=True;
    except:
        pass;
    return(out);

def toArray(obj):
    """
    toArray     Converts a string or object into an array
                It is is just one object, it will be 1 length array
                If it is a string, it will split it into characters
    """
    o=[];
    if(isIterable(obj)):
        for f in obj:
            try:
                o.append(f);
            except:
                o.append(null);
    else:
        try:
            o.append(obj);
        except:
            o.append(null);
    return(o);

def instr(*vargs):
    """
    instr(n,haystack,needle)
    instr(haystack,needle)
    """
    out=-1;
    ins="";
    needle="";
    fromChar=0;
    args=list(vargs);
    if(len(args)==3):
        try:
            fromChar=0+popFirst(args);
        except:
            pass;
    if(len(args)==2):
        try:
            haystack=popFirst(args);
            needle=popFirst(args);
            ins=""+haystack[fromChar:];
        except:
            pass;
    if(needle in ins):
        out=fromChar+ins.find(needle);
    return(out);

#alias
reverse=rev;
upper=toUpper;
lower=toLower;
count=len;
strrev=rev;
strlen=len;
strpos=instr;
#repr=str;
implode=join;
explode=split;
mid=substr;

if __name__=='__main__':
    echo (APP+LOADED);
    echo (version);
    echo (typeOf(ALIAS_H));
    echo (reverse("casa"));
    echo (count("casa"));
    echo (str(null));
    echo (toTitle("martinez bas"));
    echo (substr("la casa roja",-5,2));
    echo (substr("la casa roja",0,2));
    

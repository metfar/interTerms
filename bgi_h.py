#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bgi_h.py
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
  

import sys;
import shlex;

from random import random;

try:
	import os;
	import contextlib;
	from pprint import pprint;
	with contextlib.redirect_stdout(None):
		import pygame;
		from pygame.locals import *;
	pygame.mixer.pre_init(22050, -16, 1,16384);
	pygame.mixer.init();
	channel=pygame.mixer.find_channel(True);
	#pygame.mixer.music.load(arch);
	#pygame.mixer.music.play();
	#arch="/home/wmartinez/bin/sound/ok.ogg";
	#sound1=pygame.mixer.Sound(arch);
	#channel.set_volume(0.5);
	#channel.play(sound1);
	#while channel.get_busy() == True:
	#  continue;
	#channel.stop();
	#sys.exit(0);
except:
	sys.exit(1);

from math_h import *;

def split(source):
	return(shlex.split(source,posix=False,comments=True));
def isset(var):
	return(var in locals() or var in globals());

_B=2;
_K=_B**10;_M=_K**2;_G=_K**3;
for f in range(0,24):
	mem=(_B**f);
	val=(_B**f)*_K;
	exec("M"+str(mem)+"K="+str(val));
	
_PC=1;
_LIMMEM=M64K;
_SCR=M16K;
"""
for f in locals():
	if "M" in f.upper():
		print(f);
exit(1);"""
TABBG=(20,20,50);
TABINK=(235,235,205);
if not (isset("nx") or isset("ny")):
	sx,sy=512,256;
	nx,ny=640,480;

if not (isset("sx") or isset("sy")):
	sx,sy=512,256;

if sx>nx:
	nx=sx;

if sy>ny:
	ny=sy;

pygame.init();

window = pygame.display.set_mode((nx,ny));

def set_title(title=NULL):
	if title==NULL:
		pygame.display.set_caption(__name__);
	else:
		pygame.display.set_caption(title);

def set_icon(img=NULL):
	try:
		icon = pygame.image.load(img);
		pygame.display.set_icon(icon);
	except:
		pass;

clock = pygame.time.Clock();

pixel=pygame.Surface((1,1));

x,y=0,0;
run = True;
somethingChanged=True;
KEYPRESSED=set();
COLOURS=pal(0);
COL_NAMES=[	"black",		"blue",		"red",			"magenta",
			"green",		"cyan",		"yellow",		"white",
			"brightblack", 	"brightblue","brightred", 	"brightmagenta",
			"brightgreen", "brightcyan","brightyellow",  "brightwhite"];
COLS=[COLOURS[f] for f in COL_NAMES ];
#print(COLOURS);

def invert(x,top=255):
	out=[];
	try:
		for f in x:
			out.append(top ^ f);
	except:
		for f in INK:
			out.append(top ^ f);
	return(out);
	

def color(num):
	if(type(num)==type(1)):
		return(COLS[num]);
	if(type(num)==type("a")):
		if(num in COLOURS):
			return(COLOURS[num]);
	return(INK);

RR_LENGTH=64;#This System Round Robin Length
#Noise Round Robin,IndeX
NOISE_RR=[0]*RR_LENGTH;NOISE_IX=0;

class Clk:
	_RR=[0]*RR_LENGTH;
	_IX=0;
	_value=0;
	_time=0;
	_lim=128;
	_limJmp=4;
	_states=["Low","toHi","Hi","toDown"];
	def __init__(self):
		self._status=0;
		self._values=[-(self._lim/2),0,(self._lim/2),0];
	
	def __next__(self):
		self._status=(self._status+1)%len(self._states);
		return(self._status);
	def __prior__(self):
		self._status=(self._status-1)%len(self._states);
		return(self._status);
	
	def __last__(self):
		return((self._status-1)%len(self._states));
	def __following__(self):
		return((self._status+1)%len(self._states));
	
	def status(self):
		return(self._status);
	
	def text_status(self):
		return(self._states[self._status]);
	
	def value(self):
		delta=self.__next__()-self.__last__();
		return(self._values[self._status]+NOISE_RR[NOISE_IX]);
	
	def tick(self):
		self._time+=1;
		if(self._time>self._lim):
			self._time=0;
			self.__next__();
		
		self._IX=(self._IX+1)%RR_LENGTH;
		self._RR[self._IX]=self.value();

	def RR(self):
		return(self._RR);
	def IX(self):
		return(self._IX);

CLK=Clk();

class FlagReg:
	def __init__(self):
		
		self._FLAG=0;
	
	#get
	def getSF(self):#SIGN
		return(0<(self._FLAG & 128));
	
	def getZF(self):#ZERO
		return(0<(self._FLAG &  64));
	
	def getEF(self):#ERROR
		return(0<(self._FLAG &  32));
	
	def getHF(self):#HALF_CARRY
		return(0<(self._FLAG &  16));
	
	def getWF(self):#WARNING
		return(0<(self._FLAG &   8));
	
	def getOF(self):#PARITY_OVERFLOW
		return(0<(self._FLAG &   4));
	
	def getAF(self):#ADD_SUBTRACT
		return(0<(self._FLAG &   2));
	
	def getCF(self):#CARRY
		return(0<(self._FLAG &   1));
	
	#set
	def setSF(self):#SIGN
		self._FLAG = (self._FLAG | 128);
	
	def setZF(self):#ZERO
		self._FLAG = (self._FLAG |  64);
	
	def setEF(self):#ERROR
		self._FLAG = (self._FLAG |  32);
	
	def setHF(self):#HALF_CARRY
		self._FLAG = (self._FLAG |  16);
	
	def setWF(self):#WARNING
		self._FLAG = (self._FLAG |   8);
	
	def setOF(self):#PARITY_OVERFLOW
		self._FLAG = (self._FLAG |   4);
	
	def setAF(self):#ADD_SUBTRACT
		self._FLAG = (self._FLAG |   2);
	
	def setCF(self):#CARRY
		self._FLAG = (self._FLAG |   1);
	
	#reset
	#set
	def resetSF(self):#SIGN
		self._FLAG = (self._FLAG ^ 128);
	
	def resetZF(self):#ZERO
		self._FLAG = (self._FLAG ^  64);
	
	def resetEF(self):#ERROR
		self._FLAG = (self._FLAG ^  32);
	
	def resetHF(self):#HALF_CARRY
		self._FLAG = (self._FLAG ^  16);
	
	def resetWF(self):#WARNING
		self._FLAG = (self._FLAG ^   8);
	
	def resetOF(self):#PARITY_OVERFLOW
		self._FLAG = (self._FLAG ^   4);
	
	def resetAF(self):#ADD_SUBTRACT
		self._FLAG = (self._FLAG ^   2);
	
	def resetCF(self):#CARRY
		self._FLAG = (self._FLAG ^   1);
	
	#toggle
	def toggleSF(self):#SIGN
		if(self.getSF()):
			self.resetSF();
		else:
			self.setSF();
		
	def toggleZF(self):#ZERO
		if(self.getZF()):
			self.resetZF();
		else:
			self.setZF();
		
	def toggleEF(self):#ERROR
		if(self.getEF()):
			self.resetEF();
		else:
			self.setEF();
		
	def toggleHF(self):#HALF_CARRY
		if(self.getHF()):
			self.resetHF();
		else:
			self.setHF();
		
	def toggleWF(self):#WARNING
		if(self.getWF()):
			self.resetWF();
		else:
			self.setWF();
		
	def toggleOF(self):#PARITY_OVERFLOW
		if(self.getOF()):
			self.resetOF();
		else:
			self.setOF();
		
	def toggleAF(self):#ADD_SUBTRACT
		if(self.getAF()):
			self.resetAF();
		else:
			self.setAF();
		
	def toggleCF(self):#CARRY
		if(self.getCF()):
			self.resetCF();
		else:
			self.setCF();
	
	def set(self,value=255):
		try:
			self._FLAG=value;
		except:
			pass;
	
	def reset(self):
		self.set(0);
	
	def get(Self):
		return(self._FLAG);
	
	def __repr__(self):
		return(("%8s" % bin(127)[2:]).replace(" ","0"));


def plot(surf,pos,colour=NULL):
	global pixel;
	rpos=[];
	if (colour==NULL):
		colour=INK;
	for f in pos:
		rpos.append(int(f));
	pixel.fill(colour);
	surf.blit(pixel,rpos);
	#pygame.draw.rect(surf,colour,[rpos,(1,1)],2); 

def rectangle(surf,start,end,colour,width=1):
	END=[abs(end[0]-start[0]),abs(end[1]-start[1])];
	pygame.draw.rect(surf,colour,[start,END],width);

def line(surf,start,end,colour,width=1):
	pygame.draw.line(surf,colour,[int(start[0]),int(start[1])],[int(end[0]),int(end[1])],width);

def box(surf,start,end,colour):
	END=(abs(end[0]-start[0]),abs(end[1]-start[1]));
	pygame.draw.rect(surf,colour,[start,END],0);
	
def cfa(surf, pos, radio, colour, width=1):
	pygame.draw.circle(surf, colour, pos, radio, width);

def circle(surf, pos, radio, colour):
	pygame.draw.circle(surf, colour, pos, radio, 0);

def clrscr(surf,colour=NULL):
	global BG;
	if colour!=NULL:
		BG=colour;
	surf.fill(BG);

def gprintf(*vargs):
	"""
	gprintf(surf,(x,y),"%FORMAT",var1,var2,...);
	"""
	args=list(vargs);
	try:
		surf=args.pop(0);
		pos=args.pop(0);
		FORMAT=args.pop(0);
		text = FONT.render((FORMAT % tuple(args)), True, color(7));
		tr = text.get_rect();
		surf.blit(text, [int(tr[0]+pos[0]),int(tr[1]+pos[1]),int(tr[2]),int(tr[3])]);
	except:
		pass;

DWMax=float(2**32);
def abs(x):
	try:
		return(-x if x<0 else x);
	except:
		return(0);
	
def rnd(minim=-32,maxim=32,precision=.0001):
	delta=abs(maxim-minim)/precision;
	n=int(random()*delta)*precision+minim;
	return(n);

	

col=0;
HZ=50.0;
INK=color(col);
BG=color(7);
TIME=0;
FONT = pygame.font.SysFont("ConsolaN.ttf", 16);
timer_event = pygame.USEREVENT;

pygame.time.set_timer(timer_event, int(1000/HZ));
start_ticks=pygame.time.get_ticks();
tick=0;

def main(args):
	set_title("BGI_H");
	set_icon("icon.png");
	return(0);

if __name__ == '__main__':
	sys.exit(main(sys.argv));

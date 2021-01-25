#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  base.py
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
#  This is part of interTerms Project < https://github.com/metfar/interTerms >
  


from bgi_h import *;

def draw(window):
	global TIME,CLK;
	#HUB
	box(window,(sx+1,0),(nx,sy+1),TABBG);
	box(window,(0,sy+1),(nx,ny),TABBG);
	#text = FONT.render(str(TIME), True, color(7));
	#text_rect = text.get_rect(center = window.get_rect().center);
	#window.blit(text, text_rect);
	rectangle(window,(10,sy+2),(sx-10,ny-50),color(9));
	RR=CLK.RR();
	IX=CLK.IX();
	HIGH=abs(ny-51-(sy+3));
	lx=10;
	data=(RR[0]+128)/256*HIGH;
	last=(10,ny-51-data);
	scx=4;
	box(window,(lx,sy+3),(sx-10,ny-51),color(7));
	
	circle(window,(128,128),64,color(4));
	cfa(window,(128,128),64,color(3));
	
	for f in range(1,len(RR)):
		nwx=10+f*scx;
		line(window,(lx,sy+3+HIGH/2),(nwx,sy+3+HIGH/2),color(0));
		lx=nwx;
		data=((64 if RR[f]>0 else -64)+128)/256*HIGH;
		NEW=(nwx,ny-51-data);
		line(window,last,NEW,color(1));
		last=NEW;
		if(f==IX):
			line(window,last,[last[0]+scx,last[1]],color(1));
			plot(window,last,color(2));
		else:
			line(window,last,[last[0]+scx,last[1]],color(6));
		
		#line(window,last,(lx,sy+3+HIGH/2),color(4));
		
	gprintf(window,[sx/2,ny-49],"Pulses:%5.1f",TIME/HZ);
	gprintf(window,[sx/2,ny-20],"Noise:%5i",NOISE_RR[NOISE_IX]);
	
	gprintf(window,[sx/2,ny-10],"CLK:%5s",CLK.text_status());

class Mem:
	def __init__(self,length=NULL):
		if(length==NULL):
			self._LENGTH=M64K;
		else:
			self._LENGTH=length;
			
		self._FULLMEM=[0]*self._LENGTH;
		self._MAR=0;
		self._LINE=16;
		self._START=1;
		self._BLOCK=2;#2==WORD,1==BYTE
		self._FLAG=FlagReg();
	
	def flag(self):
		return(self._FLAG);
	
	def __repr__(self):
		out="";
		for row in range(self._START,self._LENGTH,16):
			out+="%04x: "%(row-row%self._LINE);
			for col in range(0,self._LINE):
				out+="%02x "%(self._FULLMEM[row+col]);
				
			out+="\n";
		return(out);
	def addr(self,pos=NULL):
		if (pos==NULL):
			pos=self._MAR;
		else:
			self._MAR=pos % self._LENGTH;
		if(self._MAR<self._START):
			self._MAR=self._START;
		self._MAR=pos;
		return(pos);
	def setAddr(self,pos=NULL):
		self.addr(pos);
		
	def addrNext(self):
		self.addr(self._MAR+1);
		return(self._MAR);
	
	def addrPrev(self):
		self.addr(self._MAR-1);
		return(self._MAR);
	
	def get(self):
		out=0;
		try:
			out=self._FULLMEM[self._MAR];
			self._FLAG.resetEF();
		except:
			self._FLAG.setEF();
		return(out);
	
	def set(self,value=NULL):
		out=0;
		if(value==NULL):
			value=0;
		elif(type(value)==type("a")):
			value=ord(value[0]);
		elif(type(value)==type(0)):
			value=value % (2**(8*self._BLOCK));
			s=0 if value>=0 else 1;
			i=int(value);
			
		elif(type(value)==type(0.0)):#fld
			s=0 if value>=0 else 1;
			value=abs(value);
			i=int(value);
			d=(value-i);
			e=i/abs(value);
		try:
			self._FULLMEM[self._MAR]=value;
			self._FLAG.resetEF();
		except:
			self._FLAG.setEF();
		return(out);
	
	
	def reprRange(self,start=NULL,end=NULL):
		out="";
		if (end==NULL):
			end=self._LENGTH;
		end=end % self._LENGTH;
		
		if(start==NULL):
			start=self._START;
		
		end=	end   % self._LENGTH;
		start=	start % self._LENGTH;
		
		for row in range(start,end,16):
			out+="%04x: "%(row-row%self._LINE);
			for col in range(0,self._LINE):
				out+="%02x "%(self._FULLMEM[row+col]);
				
			out+="\n";
		return(out);



def main(args):
	global window,BG,tick,TIME,HZ,NOISE_IX,NOISE_RR,INK;
	col=0;
	MEM=Mem();
	NUM_KEYS=[
			K_0, 	K_1, 	K_2, 	K_3,
			K_4, 	K_5, 	K_6, 	K_7,
			K_8, 	K_9, 	K_KP0, 	K_KP1,
			K_KP2,	K_KP3,	K_KP4,	K_KP5,
			K_KP6,	K_KP7,	K_KP8,	K_KP9,
			K_PERIOD, K_MINUS,K_PLUS, K_SLASH, 
			K_ASTERISK, K_LEFTPAREN,K_RIGHTPAREN, K_CARET];
	
	COLKEYS=[
			K_0, 	K_1, 	K_2, 	K_3,
			K_4, 	K_5, 	K_6, 	K_7,
			K_KP0,	K_KP1,	K_KP2,	K_KP3,
			K_KP4,	K_KP5,	K_KP6,	K_KP7 ];
	SHIFTKEYS=[
			K_LSHIFT,	K_RSHIFT,	K_LCTRL,	K_RCTRL,
			K_LALT,		K_RALT,		K_LMETA,	K_RMETA,
			K_LSUPER,	K_RSUPER,	K_MODE			];
	
	print(MEM.reprRange(0,100));
	set_title("Ensamble");
	set_icon("icon.png");
	clrscr(window);
	run=true;
	x,y=0,0;
	while run:
		clock.tick(HZ);
		for event in pygame.event.get():
			if event.type == timer_event:
				TIME+=1;
				NOISE_IX=(NOISE_IX+1)%RR_LENGTH;
				NOISE_RR[NOISE_IX]=rnd(-7,7);
				CLK.tick();
			if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				run = False;
			if event.type==pygame.KEYDOWN:
				KEYPRESSED.add(event.key);
			elif event.type==pygame.KEYUP:
				KEYPRESSED.discard(event.key);
		if x<sx and (pygame.K_RIGHT in KEYPRESSED or pygame.K_d in KEYPRESSED):
			x+=1;
		if x>0  and (pygame.K_LEFT in KEYPRESSED or pygame.K_a in KEYPRESSED):
			x-=1;
		if y<sy and (pygame.K_DOWN in KEYPRESSED or pygame.K_s in KEYPRESSED or pygame.K_x in KEYPRESSED):
			y+=1;
		if y>0  and (pygame.K_UP in KEYPRESSED or pygame.K_w in KEYPRESSED):
			y-=1;
		if pygame.K_SPACE in KEYPRESSED:
			col+=1;
			col=col % len(COLOURS);
			BG=color(col);
			INK=invert(BG,189);
			#color(len(COLOURS)-col)
			#print(BG,"&&",INK);
		for f in range(0,len(COLKEYS)):
			if (COLKEYS[f] in KEYPRESSED):
				col=f%8;
				if((K_LSHIFT in KEYPRESSED) or (K_RSHIFT in KEYPRESSED)):
					col+=8;
				
				#col=col % len(COLOURS);
				BG=color(col);
				INK=invert(BG,189);
				
		if pygame.K_t in KEYPRESSED:
			print([abs(f)>10 for f in CLK.RR()]);
			
		clrscr(window,BG);
		draw(window);
		sz=8;
		for f in range(sz):
			for n in range(sz*2):
				plot(window,(x+f,y+n),invert(BG));
		somethingChanged=False;
		tick=0 if tick==7 else 7;
		plot(window,(sx,sy),color(tick));
		pygame.display.flip();
		
	pygame.quit();
	return(0);

if __name__ == '__main__':
	sys.exit(main(sys.argv));

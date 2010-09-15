# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.
# 
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

from __init__ import * #@UnusedWildImport
from angle import Angle as Angle

__author__ = '$Author$'
__version__ = '$Revision$'
__date__ = '$Date$'
__id__= '$Id$'

#	POINT EXCEPTIONS 
class PointError(Exception):
	'''
	exception handler for point
	'''
	def __init__(self,value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)
	
#	VECTOR EXCEPTIONS 
class VectorError(Exception):
	'''
	exception handler for vector
	'''
	def __init__(self,value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)
		
#	Point CLASS
class Point(object):
	"""
	Point class
	"""	
	def __init__ (self,vec=[0.0,0.0,0.0,1.0]):	
		self.vec=[0.0,0.0,0.0,1.0]	
		
		if not len(vec) <= 4:
			raise PointError("Wrong size Vector")
				
		pop=self.vec.pop
		insert=self.vec.insert
		
		for i in xrange(len(vec)):
			pop(i)
			insert(i,float(vec[i]))
			
		return
		
	def __getitem__(self, index):
		return self.vec[index]
		
	def __setitem__(self,index,value):
		self.vec[index]=float(value)	
	
	def __repr__(self):
		return repr(self.vec)
	
	def __eq__ (self,other):
		"""
		override ==
		"""
		if (isinstance(other, Point)):
			return (self.vec == other.vec)
		
		if (isinstance(other, list)) or (isinstance(other, tuple)):
			if (self.vec == other) or (self.vec[:3] == other):
				return True
		
		else:
			return False
	
	def __ne__(self,other):
		"""
		override !=
		"""
		if (isinstance(other, Point)):
			return (self.vec != other.vec)
		
		if (isinstance(other, list)) or (isinstance(other, tuple)):
			if (self.vec != other) or (self.vec[:3] != other):
				return True
			
		else:
			return False
	
	def __add__(self,other):
		if (isinstance(other, Vector)):
			'''
			Translate point P by vector v. 
			'''
			return Vector(map(lambda x, y: x+y, self[:3], other[:3]))		
		
		elif (isinstance(other, Point)):
			raise PointError,"Operation Not Allowed for type %s"%type(other)
		
		else:
			pass
			
				
	def __sub__(self,other):
		"""
		override -
		"""
		if (isinstance(other, Point)):
			'''
			difference between two points. 
			'''
			return Vector(map(lambda x, y: x-y, self[:3], other[:3]))
		
		elif (isinstance(other, Vector)):
			return Point(map(lambda x, y: x-y, self[:3], other[:3]))
			
		
		else:
			raise PointError,"Operation Not Allowed for type %s"%type(other)
					
	def __mul__(self,other):
		"""
		override *
		"""
		Vmul=[]
		append=Vmul.append
				
		if isinstance(other,float) or isinstance(other,int):
			for i in xrange(3):
				append(self.vec[i]*float(other))
				
		else:
			raise PointError("Operation Not Allowed for type %s"%type(other))
		
		return Point(Vmul)
		
	def __div__(self,other):
		"""
		override /
		""" 
		Vdiv=[]
		append=Vdiv.append
				
		if isinstance(other,float) or isinstance(other,int):
			for i in xrange(3):
				append(self.vec[i]/float(other))				
		else:
			raise PointError("Operation Not Allowed for type %s"%type(other))
				
		return Point(Vdiv)
				
	def __len__(self):
		return len(self.vec)


#	VECTOR CLASS
class Vector(Point):
	"""
	Vector class
	"""	
	def __init__ (self,vec=[0.0,0.0,0.0,1.0]):
		super(Vector,self).__init__(vec)				
		return
	
	def __add__(self,other):
		"""
		override +
		"""
		if (isinstance(other, Vector)):
			return Vector(map(lambda x, y: x+y, self[:3], other[:3]))

		else:
			raise VectorError("Operation Not Allowed for type %s"%type(other))
		
	#	PUBLIC
	def mag( self ):
		"""
		magnitude of vector
		"""
		Vsub=0.0
		
		for i in xrange(3):
			Vsub +=(self.vec[i] * self.vec[i])
				
		return math.sqrt(Vsub) 
		
	def normalize( self ):
		"""
		normalize vector
		"""
		retV=[]
		insert = retV.insert
		mag = self.mag()
		if math.fabs(mag) > EPSILON:
			imag=1.0/mag
			for i in xrange(3):
				insert(i, self.vec[i]*imag)
			return Vector(retV)
		else :
			print 'warning! magnitude == 0 '
			return None
		
	def dot(self,other):
		"""
		dot product
		"""
		Vsub=0.0
		for i in xrange(3):
			Vsub +=(self.vec[i] * other.vec[i])
		
		return Angle(Vsub)
		
	def cross(self,other):
		"""
		cross product
		"""
		Cross=[0.0,0.0,1.0]
		
		ov=other.vec
		sv=self.vec
		
		Cross[0]= (ov[2] * sv[1])-(sv[2] * ov[1])
		Cross[1]= (-sv[0] * ov[2]) + (sv[2] * ov[0])
		Cross[2]= (sv[0]*ov[1])-(sv[1]*ov[0])
		return Vector(Cross)
		
	def angleBetween( self, other ):
		"""
		angle between vectors
		"""
		
		NS = self.normalize()
		NO = other.normalize()
		
		ND = NS.dot(NO)
				
		return Angle(math.acos(ND))
		
	def wPos(self,p2,w=.5):
		"""
		weighted Point betweeb vectors
		"""
		
		dist=p2-self
		absVal=[]
		append=absVal.append
		for i in xrange(3):
			append((dist.vec[i]*w)+self.vec[i])
		return Vector(absVal)